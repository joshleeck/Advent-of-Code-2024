import numpy as np
from queue import Queue


def bfs(M, vis, start, end):
    queue = Queue()
    queue.put([start])  # Enqueue the start position

    while not queue.empty():
        path = queue.get()  # Dequeue the path
        j, i = path[-1]     # Current position is the last element of the path

        if (j, i) == end:
            return path  # Return the path if end is reached

        for dj, di in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Possible movements
            next_j, next_i = j + dj, i + di
            if M[next_j, next_i] != '#' and (next_j, next_i) not in path and not vis[next_j, next_i]:
                new_path = list(path)
                new_path.append((next_j, next_i))
                vis[next_j, next_i] = True
                queue.put(new_path)  # Enqueue the new path


def get_shortcut_path(start, j_diff, i_diff):
    shortcut_path = []
    if j_diff < 0:
        for jj in range(-1, j_diff-1, -1):
            step = (start[0] + jj, start[1])
            shortcut_path.append(step)
    elif j_diff >= 0:
        for jj in range(1, j_diff+1, 1):
            step = (start[0] + jj, start[1])
            shortcut_path.append(step)

    if j_diff == 0:
        last_step = start
    else:
        last_step = step

    if i_diff < 0:
        for ii in range(-1, i_diff-1, -1):
            step = (last_step[0], last_step[1] + ii)
            shortcut_path.append(step)
    elif i_diff >= 0:
        for ii in range(1, i_diff+1, 1):
            step = (last_step[0], last_step[1] + ii)
            shortcut_path.append(step)

    return shortcut_path


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_20.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    M = np.array(M, dtype=object)

    # Part 1
    # Make a visited matrix to populate to avoid infinite loops, just to be safe (also to re-use Day 18 code...)
    vis = M.copy()
    for j in range(vis.shape[0]):
        for i in range(vis.shape[1]):
            vis[j, i] = False

    start = (np.where(M == 'S')[0][0], np.where(M == 'S')[1][0])
    end = (np.where(M == 'E')[0][0], np.where(M == 'E')[1][0])

    # Benchmark
    path = bfs(M, vis, start, end)

    for index in path:  # Lay the path for easier referencing
        M[index] = 'O'

    count = 0
    save = 100
    for j in range(1, M.shape[0]-1):
        for i in range(1, M.shape[1]-1):
            if M[j, i] == '#':
                N = M.copy()
                neighbours = [(j-1, i), (j+1, i), (j, i+1), (j, i-1)]
                cut = [neighbour for neighbour in neighbours if M[neighbour] == 'O']
                if len(cut) == 2:  # A shortcut exists
                    # Need to -1 as time taken to execute cut
                    shortcut = abs(path.index(cut[0]) - path.index(cut[1])) - 1
                    if shortcut >= save:
                        count += 1

    print(count)  # Correct

    # Part 2
    count = 0
    max_steps = 20
    shortcut_paths = []
    for i in range(len(path)-save):
        start_cut = path[i]
        print(start_cut)
        end_cut = path[i+save:]
        for end in end_cut:
            space_diff = np.subtract(end, start_cut)
            j_diff = space_diff[0]
            i_diff = space_diff[1]
            shortcut_path = get_shortcut_path(start_cut, j_diff, i_diff)
            steps_required = abs(space_diff[0]) + abs(space_diff[1])
            if steps_required <= max_steps and abs(path.index(start_cut) - path.index(end)) - steps_required >= save:
                shortcut_paths.append(shortcut_path)

    print(len(shortcut_paths))  # Correct


