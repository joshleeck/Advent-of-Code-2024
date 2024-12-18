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


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_18.txt'

    bytes = []
    with open(filename, "r") as f:
        for line in f:
            byte = line.strip().split(',')
            bytes.append((int(byte[1]), int(byte[0])))

    space = 70
    start = (0 + 1, 0 + 1)  # Accounting for padding
    end = (space + 1, space + 1)
    fallen = 1024

    M = np.zeros((space+1, space+1), dtype=object)
    M[M == 0] = '.'

    # Part 1
    for byte in bytes[:fallen]:
        M[byte] = '#'

    # Apply padding on walls of space
    M = np.hstack((M, np.zeros((M.shape[0], 1))))
    M = np.hstack((np.zeros((M.shape[0], 1)), M))
    M = np.vstack((M, np.zeros((1, M.shape[1]))))
    M = np.vstack((np.zeros((1, M.shape[1])), M))
    M[M == 0] = '#'

    # Make a visited matrix to populate to avoid infinite loops
    vis = M.copy()
    for j in range(vis.shape[0]):
        for i in range(vis.shape[1]):
            vis[j, i] = False

    # Apply algorithm
    path = bfs(M, vis, start, end)

    # Exclude starting point
    print(len(path)-1)  # Correct

    # Part 2
    # Trial and error seems fast enough, path is None if bfs cannot find a path to exit

    M = np.zeros((space+1, space+1), dtype=object)
    M[M == 0] = '.'
    fallen = 2966  # 2966 bytes still allows a path, but not 2967

    for byte in bytes[:fallen]:
        M[byte] = '#'

    # Apply padding on walls of space
    M = np.hstack((M, np.zeros((M.shape[0], 1))))
    M = np.hstack((np.zeros((M.shape[0], 1)), M))
    M = np.vstack((M, np.zeros((1, M.shape[1]))))
    M = np.vstack((np.zeros((1, M.shape[1])), M))
    M[M == 0] = '#'

    # Make a visited matrix to populate to avoid infinite loops
    vis = M.copy()
    for j in range(vis.shape[0]):
        for i in range(vis.shape[1]):
            vis[j, i] = False

    # Apply algorithm
    path = bfs(M, vis, start, end)

    # 2967th byte (remember to flip the X and Y since we stored it opposite)
    print(bytes[2966])  # Correct