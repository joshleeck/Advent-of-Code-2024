import numpy as np
import copy
import sys
np.set_printoptions(threshold=np.inf)

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_14.txt'

    robot_p = {}
    robot_v = {}
    rob_index = 0
    with open(filename, "r") as f:
        for line in f:
            robot_p[rob_index] = tuple(line.strip().split(' ')[0].split('=')[-1].split(','))
            robot_v[rob_index] = tuple(line.strip().split(' ')[1].split('=')[-1].split(','))
            rob_index += 1

    j_len = 103
    i_len = 101

    # Make grid, empty lists as elements so can store more than 1 robot
    bathroom = np.empty((j_len, i_len), dtype=object)
    for j in range(bathroom.shape[0]):
        for i in range(bathroom.shape[1]):
            bathroom[j, i] = []

    # Populate initial robot positions and velocities
    for robot_i in robot_p.keys():
        j_loc = int(robot_p[robot_i][1])
        i_loc = int(robot_p[robot_i][0])
        robot_p[robot_i] = (j_loc, i_loc)
        bathroom[j_loc, i_loc].append(robot_i)

        j_vel = int(robot_v[robot_i][1])
        i_vel = int(robot_v[robot_i][0])
        robot_v[robot_i] = (j_vel, i_vel)

    # Clone for Part 2
    robot_p2 = robot_p.copy()
    robot_v2 = robot_v.copy()
    bathroom2 = copy.deepcopy(bathroom)

    # Part 1
    seconds = 100
    for sec in range(seconds):
        for robot_i in robot_p.keys():
            # Get location as a tuple
            new_loc = ((robot_p[robot_i][0] + robot_v[robot_i][0]) % j_len,
                      (robot_p[robot_i][1] + robot_v[robot_i][1]) % i_len)

            # Update location of robot
            bathroom[robot_p[robot_i]].remove(robot_i)
            bathroom[new_loc].append(robot_i)
            robot_p[robot_i] = new_loc

    q1 = 0  # Upper left
    q2 = 0  # Upper right
    q3 = 0  # Lower left
    q4 = 0  # Lower right
    for j in range(0, int((j_len-1)/2)):
        for i in range(0, int((i_len-1)/2)):
            q1 += len(bathroom[j, i])
        for i in range(int((i_len+1)/2), i_len):
            q2 += len(bathroom[j, i])
    for j in range(int((j_len+1)/2), j_len):
        for i in range(0, int((i_len-1)/2)):
            q3 += len(bathroom[j, i])
        for i in range(int((i_len+1)/2), i_len):
            q4 += len(bathroom[j, i])

    print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)  # Correct

    # Part 2
    seconds = 10000
    for sec in range(seconds):
        for robot_i in robot_p2.keys():
            # Get location as a tuple
            new_loc = ((robot_p2[robot_i][0] + robot_v2[robot_i][0]) % j_len,
                       (robot_p2[robot_i][1] + robot_v2[robot_i][1]) % i_len)

            # Update location of robot
            bathroom2[robot_p2[robot_i]].remove(robot_i)
            bathroom2[new_loc].append(robot_i)
            robot_p2[robot_i] = new_loc

        for i in range(i_len):  # Searching every column for straight lines (which would make part of a tree)
            for j in range(20, j_len):  # Assuming straight line needs to be 20-long, very unlikely to be coincidence
                straight = [element != [] for element in bathroom2[j-20:j, i]]
                if all(straight):
                    print('Found 20-long vertical straight line')
                    print(sec + 1, 'seconds')  # Correct
                    print('Visualising...')
                    tmp = copy.deepcopy(bathroom2)
                    for row in range(j_len):
                        for col in range(i_len):
                            if tmp[row, col]:
                                tmp[row, col] = '#'
                            else:
                                tmp[row,col] = '.'
                    for row in range(j_len):
                        print(list(tmp[row, :]))
                    sys.exit()
