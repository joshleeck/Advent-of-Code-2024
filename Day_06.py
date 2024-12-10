import numpy as np

def move(M, direc, leave_area, n_overlap):
    x = np.where(M == '^')[0][0], np.where(M == '^')[1][0]
    n_overlap += 1  # Default assume overlap, unless handled below
    if direc == 'up':
        # Move
        if x[0]-1 >= 0 and M[x[0]-1, x[1]] != '#':
            if M[x[0]-1, x[1]] != 'X':
                n_overlap = 0
            M[x[0]-1, x[1]] = '^'
            M[x] = 'X'
        elif x[0]-1 < 0:
            leave_area = True
            M[x] = 'X'
        # Turn
        elif M[x[0]-1, x[1]] == '#':
            direc = 'right'

    if direc == 'right':
        # Move
        if x[1]+1 <= M.shape[1]-1 and M[x[0], x[1]+1] != '#':
            if M[x[0], x[1]+1] != 'X':
                n_overlap = 0
            M[x[0], x[1]+1] = '^'
            M[x] = 'X'
        elif x[1]+1 > M.shape[1]-1:
            leave_area = True
            M[x] = 'X'
        # Turn
        elif M[x[0], x[1]+1] == '#':
            direc = 'down'

    if direc == 'down':
        # Move
        if x[0]+1 <= M.shape[0]-1 and M[x[0]+1, x[1]] != '#':
            if M[x[0]+1, x[1]] != 'X':
                n_overlap = 0
            M[x[0]+1, x[1]] = '^'
            M[x] = 'X'
        elif x[0]+1 > M.shape[0]-1:
            leave_area = True
            M[x] = 'X'
        # Turn
        elif M[x[0]+1, x[1]] == '#':
            direc = 'left'

    if direc == 'left':
        # Move
        if x[1]-1 >= 0 and M[x[0], x[1]-1] != '#':
            if M[x[0], x[1]-1] != 'X':
                n_overlap = 0
            M[x[0], x[1]-1] = '^'
            M[x] = 'X'
        elif x[1]-1 < 0:
            leave_area = True
            M[x] = 'X'
        # Turn
        elif M[x[0], x[1]-1] == '#':
            direc = 'up'

    return M, direc, leave_area, n_overlap

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_06.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    N = np.array(M)
    M = N.copy()

    # Part 1
    direc = 'up'
    left_area = False
    n_overlap = 0
    while not left_area:
        M, direc, left_area, n_overlap = move(M, direc, left_area, n_overlap)

    #print(M)
    print(np.sum(M == 'X'))  # Correct

    # Part 2
    # Brute force, sub-optimal but little code
    P = M.copy()
    P[P == '.'] = 'o'  # Prepping for later
    count = 0
    for j in range(N.shape[0]):
        for i in range(N.shape[1]):
            print(j, i)
            M = N.copy()
            M[P == 'o'] = 'o'
            if M[j,i] == '^':  # Original location which we cannot place blockade
                continue
            if M[j,i] == '#':  # Already have blockade so we cannot place blockade
                continue
            if M[j,i] == 'o':  # Guard never passes this portion anyway, so no need blockade here
                continue
            # Place obstruction
            M[j,i] = '#'
            direc = 'up'
            left_area = False
            n_overlap = 0
            while not left_area:
                M, direc, left_area, n_overlap = move(M, direc, left_area, n_overlap)
                if n_overlap > 1000:  # In a loop if consecutive overlap (for 130 x 130 grid)
                    count += 1
                    print('Found infinite loop')
                    break

    print(count)  # Correct