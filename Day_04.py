import numpy as np

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_04.txt'

    # Write file contents into matrix
    M = []
    with open (filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    M = np.array(M)
    print(M.shape)

    # Part 1
    count = 0
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i] == 'X':
                # Right
                if ''.join(list(M[j, i:i+4])) == 'XMAS':
                    count += 1
                # Left
                if ''.join(list(M[j, i-3:i+1])) == 'SAMX':
                    count += 1
                # Down
                if ''.join(list(M[j:j+4, i])) == 'XMAS':
                    count += 1
                # Up
                if ''.join(list(M[j-3:j+1, i])) == 'SAMX':
                    count += 1
                # Down Right
                if j <= M.shape[0] - 4 and i <= M.shape[1] - 4:
                    phr = M[j,i] + M[j+1,i+1] + M[j+2,i+2] + M[j+3,i+3]
                    if phr == 'XMAS':
                        count += 1
                # Down Left
                if j <= M.shape[0] - 4 and i >= 3:
                    phr = M[j,i] + M[j+1,i-1] + M[j+2,i-2] + M[j+3,i-3]
                    if phr == 'XMAS':
                        count += 1
                # Up Right
                if j >= 3 and i <= M.shape[1] - 4:
                    phr = M[j,i] + M[j-1,i+1] + M[j-2,i+2] + M[j-3,i+3]
                    if phr == 'XMAS':
                        count += 1
                # Up Left
                if j >= 3 and i >= 3:
                    phr = M[j,i] + M[j-1,i-1] + M[j-2,i-2] + M[j-3,i-3]
                    if phr == 'XMAS':
                        count += 1

    print(count)  # Correct

    # Part 2
    count2 = 0
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if (1 <= j <= M.shape[0] - 2) and (1 <= i <= M.shape[1] - 2):
                if M[j, i] == 'A':
                    rad = M[j-1,i-1] + M[j-1,i+1] + M[j+1,i-1] + M[j+1,i+1]
                    # All permutations require 2 M and 2 S around A, same letter on same sides
                    if rad == 'MMSS' or rad == 'MSMS' or rad == 'SSMM' or rad == 'SMSM':
                        count2 += 1

    print(count2)  # Correct
