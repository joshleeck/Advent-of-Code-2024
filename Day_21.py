import numpy as np
from queue import Queue
import re
import itertools


def bfs(M, vis, start, end, search):
    queue = Queue()
    queue.put([start])  # Enqueue the start position

    while not queue.empty():
        path = queue.get()  # Dequeue the path
        j, i = path[-1]  # Current position is the last element of the path

        if (j, i) == end:
            return path  # Return the path if end is reached

        # The order of search matters for the robots!
        for dj, di in search:  # Possible movements
            next_j, next_i = j + dj, i + di
            if M[next_j, next_i] != '#' and (next_j, next_i) not in path and not vis[next_j, next_i]:
                new_path = list(path)
                new_path.append((next_j, next_i))
                vis[next_j, next_i] = True
                queue.put(new_path)  # Enqueue the new path


def make_nkeypad_dict(keypad_array, search):
    seq_nkp = {}
    for num_st in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']:
        num_dict = {}
        for num_end in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']:
            # Apply padding around keypad to simulate maze
            M = keypad_array.copy()

            M = np.hstack((M, np.zeros((M.shape[0], 1))))
            M = np.hstack((np.zeros((M.shape[0], 1)), M))
            M = np.vstack((M, np.zeros((1, M.shape[1]))))
            M = np.vstack((np.zeros((1, M.shape[1])), M))
            M[M == 0] = '#'

            # Get start and end indexes after padding
            start = (np.where(M == num_st)[0][0], np.where(M == num_st)[1][0])
            end = (np.where(M == num_end)[0][0], np.where(M == num_end)[1][0])

            for j in range(1, M.shape[0] - 1):
                for i in range(1, M.shape[1] - 1):
                    M[j, i] = '.'

            M[M.shape[0] - 2, 1] = '#'  # Ensure no movement to bottom left square of keypad

            # Copy of keypad array to avoid infinite loops
            vis = M.copy()
            for j in range(vis.shape[0]):
                for i in range(vis.shape[1]):
                    vis[j, i] = False

            path = bfs(M, vis, start, end, search)
            presses = []
            for index in range(len(path) - 1):
                (dj, di) = np.subtract(path[index + 1], path[index])
                if (dj, di) == (1, 0):
                    presses.append('v')
                elif (dj, di) == (0, 1):
                    presses.append('>')
                elif (dj, di) == (-1, 0):
                    presses.append('^')
                elif (dj, di) == (0, -1):
                    presses.append('<')

            # Add the shortest 'path' and presses to get from start to end
            num_dict[num_end] = presses

        # Each start will have a dictionary containing all the shortest presses to other buttons
        seq_nkp[num_st] = num_dict

    return seq_nkp


def make_dkeypad_dict(keypad_array, search):
    seq_dkp = {}
    for dir_st in ['<', '>', 'v', '^', 'A']:
        dir_dict = {}
        for dir_end in ['<', '>', 'v', '^', 'A']:
            # Apply padding around keypad to simulate maze
            M = keypad_array.copy()

            M = np.hstack((M, np.zeros((M.shape[0], 1))))
            M = np.hstack((np.zeros((M.shape[0], 1)), M))
            M = np.vstack((M, np.zeros((1, M.shape[1]))))
            M = np.vstack((np.zeros((1, M.shape[1])), M))
            M[M == 0] = '#'

            # Get start and end indexes after padding
            start = (np.where(M == dir_st)[0][0], np.where(M == dir_st)[1][0])
            end = (np.where(M == dir_end)[0][0], np.where(M == dir_end)[1][0])

            for j in range(1, M.shape[0] - 1):
                for i in range(1, M.shape[1] - 1):
                    M[j, i] = '.'

            M[1, 1] = '#'  # Ensure no movement to top left square of keypad

            # Copy of keypad array to avoid infinite loops
            vis = M.copy()
            for j in range(vis.shape[0]):
                for i in range(vis.shape[1]):
                    vis[j, i] = False

            path = bfs(M, vis, start, end, search)
            presses = []
            for index in range(len(path) - 1):
                (dj, di) = np.subtract(path[index + 1], path[index])
                if (dj, di) == (1, 0):
                    presses.append('v')
                elif (dj, di) == (0, 1):
                    presses.append('>')
                elif (dj, di) == (-1, 0):
                    presses.append('^')
                elif (dj, di) == (0, -1):
                    presses.append('<')

            # Add the shortest 'path' and presses to get from start to end
            dir_dict[dir_end] = presses

        # Each start will have a dictionary containing all the shortest presses to other buttons
        seq_dkp[dir_st] = dir_dict

    return seq_dkp


cache = {}
def recur_keypad(rkeys, n, n_max):
    if n == 0:
        return len(rkeys)

    if (tuple(rkeys), n, n_max) not in cache:
        rkeys = ''.join(rkeys)
        st = 'A'

        count = 0
        for en in rkeys + ('A' if n != n_max else ''):
            # Have to try all permutations of searching for shortest path
            searches = list(itertools.permutations([(1, 0), (-1, 0), (0, 1), (0, -1)]))
            best = None
            for search in searches:
                seq_nkp = make_nkeypad_dict(num_keypad_array, search)
                seq_dkp = make_dkeypad_dict(dir_keypad_array, search)
                if n == n_max:
                    path = seq_nkp[st]
                else:
                    path = seq_dkp[st]
                if best is None:
                    best = recur_keypad(tuple(path[en]), n - 1, n_max)
                else:
                    best = min(best, recur_keypad(tuple(path[en]), n - 1, n_max))
            count += best
            st = en
            if n == 1:
                count += 1
        cache[tuple(rkeys), n, n_max] = count

    return cache[tuple(rkeys), n, n_max]


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_21.txt'

    # Write file contents into matrix
    codes = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            codes.append(line_list)

    print(codes)

    # Part 1
    n_robots = 3
    num_keypad_array = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['#', '0', 'A']], dtype=object)
    dir_keypad_array = np.array([['#', '^', 'A'], ['<', 'v', '>']], dtype=object)

    sum = 0
    # Robot at number keypad
    for x in codes:
        code_concat = ''.join(x)
        complexity = int(re.search(r'\d+', code_concat).group())
        code = x.copy()

        # Direction key pad
        keypress_length = recur_keypad(code, n_robots, n_robots)

        print(keypress_length, complexity)
        sum += keypress_length * complexity

    print(sum)  # Correct

    # Part 2
    # Need to use cache, modified script based on Neil Thistlethwaite's Youtube video.
    # Retained use of BFS within search, but less efficient - code takes a while to run but works
    n_robots = 26
    num_keypad_array = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['#', '0', 'A']], dtype=object)
    dir_keypad_array = np.array([['#', '^', 'A'], ['<', 'v', '>']], dtype=object)

    sum = 0
    # Robot at number keypad
    for x in codes:
        code_concat = ''.join(x)
        complexity = int(re.search(r'\d+', code_concat).group())
        code = x.copy()

        # Direction key pad
        keypress_length = recur_keypad(code, n_robots, n_robots)

        print(keypress_length, complexity)
        sum += keypress_length * complexity

    print(sum)  # Correct
