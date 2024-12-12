import numpy as np


def expand_region(region, M, N, num):
    done = True
    for sq in region:
        j, i = sq
        sq_type = M[j, i]
        if j+1 <= M.shape[0]-1:
            if M[j+1, i] == sq_type and (j+1, i) not in region:
                region.append((j+1, i))
                done = False
        if j-1 >= 0:
            if M[j-1, i] == sq_type and (j-1, i) not in region:
                region.append((j-1, i))
                done = False
        if i+1 <= M.shape[1]-1:
            if M[j, i+1] == sq_type and (j, i+1) not in region:
                region.append((j, i+1))
                done = False
        if i-1 >= 0:
            if M[j, i-1] == sq_type and (j, i-1) not in region:
                region.append((j, i-1))
                done = False

    if done:
        for sq in region:
            N[sq] = '.'
            M[sq] = str(num)
        return region, M, N, num

    return expand_region(region, M, N, num)


def numofneighbour(M, j, i):
    count = 0

    if j-1 >= 0 and M[j-1, i]:
        count += 1
    if j+1 <= M.shape[0]-1 and M[j+1, i]:
        count += 1
    if i-1 >= 0 and M[j, i-1]:
        count += 1
    if i+1 <= M.shape[1]-1 and M[j, i+1]:
        count += 1

    return count


def get_region_peri(M):
    peri = 0
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i]:
                peri += (4 - numofneighbour(M, j, i))

    return peri


def get_region_peri_disc(M):
    peri = 0
    # Convolve 2 by 2 boxes and count vertices (pad matrix first)
    M_c = np.hstack((M, np.zeros((M.shape[0], 1))))
    M_c = np.hstack((np.zeros((M.shape[0], 1)), M_c))
    M_c = np.vstack((M_c, np.zeros((1, M.shape[1]+2))))
    M_c = np.vstack((np.zeros((1, M.shape[1]+2)), M_c))

    # Find top left corner of region
    tl = (min(np.where(M_c == 1)[0]), min(np.where(M_c == 1)[1]))
    for row in range(tl[0]-1, M_c.shape[0]-1):  # Convolve down rows
        for col in range(tl[1]-1, M_c.shape[1]-1):  # Convolve across columns
            if np.count_nonzero(M_c[row:row+2, col:col+2]) in [1, 3]:  # Box contains vertex
                peri += 1
            elif np.count_nonzero(M_c[row:row+2, col:col+2]) == 2:  # Diagonal so box contains two vertices
                if M_c[row, col] == M_c[row+1, col+1] or M_c[row, col] == M_c[row+1, col+1]:
                    peri += 2

    return peri


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_12.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    M = np.array(M, dtype=object)
    # For masking
    N = np.copy(M)
    # For Part 2
    O = np.copy(M)

    # Part 1
    num = 0
    areas = {}
    peris = {}
    # Find unmasked new areas to expand it recursively, then mask and repeat
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if N[j, i] != '.':
                region = [(j, i)]
                region, M, N, num = expand_region(region, M, N, num)
                areas[num] = len(region)
                num += 1

    # Second pass to compute perimeter
    for index in range(num):
        M2 = np.where(M == str(index), 1, 0)
        # Mask region
        peris[index] = get_region_peri(M2)

    sum = 0
    for key in peris:
        sum += peris[key]*areas[key]

    print('Part 1: ', sum)  # Correct

    # Part 2
    for index in range(num):
        M2 = np.where(M == str(index), 1, 0)
        # Mask region
        if np.count_nonzero(M2) == 1 or np.count_nonzero(M2) == 2:
            peris[index] = 4
        else:
            peris[index] = get_region_peri_disc(M2)

    sum = 0
    for key in peris:
        sum += peris[key]*areas[key]

    print('Part 2: ', sum)  # Correct
