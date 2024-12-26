import numpy as np


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_25.txt'

    # Write file contents into matrix
    keys = []
    locks = []
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            if not line_list:
                if M[0] == ['#', '#', '#', '#', '#']:
                    locks.append(np.array(M, dtype=object))
                elif M[0] == ['.', '.', '.', '.', '.']:
                    keys.append(np.array(M, dtype=object))
                M = []
            else:
                M.append(line_list)
        else:
            if M[0] == ['#', '#', '#', '#', '#']:
                locks.append(np.array(M, dtype=object))
            elif M[0] == ['.', '.', '.', '.', '.']:
                keys.append(np.array(M, dtype=object))

    # Part 1 and Deliver The Chronicle
    count = 0
    for key in keys:
        keycode = []
        for key_i in range(key.shape[1]):
            keycode.append(len(np.where(key[:, key_i] == '#')[0])-1)

        for lock in locks:
            lockcode = []
            for lock_i in range(lock.shape[1]):
                lockcode.append(len(np.where(lock[:, lock_i] == '#')[0])-1)

            if all(np.array(lockcode) + np.array(keycode) <= np.array([5, 5, 5, 5, 5])):
                count += 1

    print(count)  # Correct
