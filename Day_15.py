import numpy as np


def push_up(M, item_loc, item):
    j, i = item_loc
    if M[j-1, i] == '#':
        pass
    elif M[j-1, i] == 'O':
        push_up(M, (j-1, i), 'O')
    # Part 2
    elif M[j-1, i] == ']' and M[j, i] in '@[]':
        push_up(M, (j-1, i), ']')
        push_up(M, (j-1, i-1), '[')
    elif M[j-1, i] == '[' and M[j, i] in '@[]':
        push_up(M, (j-1, i), '[')
        push_up(M, (j-1, i+1), ']')

    if M[j-1, i] == '.' and (M[j, i] == '@' or M[j, i] == 'O'):
        M[j-1, i] = item
        M[j, i] = '.'
    # Part 2
    elif M[j-1, i] == '.' and M[j-1, i-1] == '.' and M[j, i] == ']':
        M[j-1, i] = ']'
        M[j-1, i-1] = '['
        M[j, i] = '.'
        M[j, i-1] = '.'
    elif M[j-1, i] == '.' and M[j-1, i+1] == '.' and M[j, i] == '[':
        M[j-1, i] = '['
        M[j-1, i+1] = ']'
        M[j, i] = '.'
        M[j, i+1] = '.'


def push_down(M, item_loc, item):
    j, i = item_loc
    if M[j+1, i] == '#':
        pass
    elif M[j+1, i] == 'O':
        push_down(M, (j+1, i), 'O')
    # Part 2
    elif M[j+1, i] == ']' and M[j, i] in '@[]':
        push_down(M, (j+1, i), ']')
        push_down(M, (j+1, i-1), '[')
    elif M[j+1, i] == '[' and M[j, i] in '@[]':
        push_down(M, (j+1, i), '[')
        push_down(M, (j+1, i+1), ']')

    if M[j+1, i] == '.' and (M[j, i] == '@' or M[j, i] == 'O'):
        M[j+1, i] = item
        M[j, i] = '.'
    # Part 2
    elif M[j+1, i] == '.' and M[j+1, i-1] == '.' and M[j, i] == ']':
        M[j+1, i] = ']'
        M[j+1, i-1] = '['
        M[j, i] = '.'
        M[j, i-1] = '.'
    elif M[j+1, i] == '.' and M[j+1, i+1] == '.' and M[j, i] == '[':
        M[j+1, i] = '['
        M[j+1, i+1] = ']'
        M[j, i] = '.'
        M[j, i+1] = '.'


def push_left(M, item_loc, item):
    j, i = item_loc
    if i-2 < 0:  # Break if at the left wall
        return None
    if M[j, i-1] == '#':
        pass
    elif M[j, i-1] == 'O':
        push_left(M, (j, i-1), 'O')
    # Part 2
    elif M[j, i-1] == ']' and M[j, i] == '@':  # Robot is right beside box
        push_left(M, (j, i-1), ']')
    elif M[j, i-2] == ']' and M[j, i] == ']':  # Box is right beside box
        push_left(M, (j, i-2), ']')

    if M[j, i-1] == '.' and (M[j, i] == '@' or M[j, i] == 'O'):
        M[j, i-1] = item
        M[j, i] = '.'
    # Part 2
    elif M[j, i-2] == '.' and M[j, i-1] == '[' and M[j, i] == ']':
        M[j, i-2] = '['
        M[j, i-1] = ']'
        M[j, i] = '.'


def push_right(M, item_loc, item):
    j, i = item_loc
    if i+2 > M.shape[1]-1:  # Break if at right wall
        return None
    if M[j, i+1] == '#':
        pass
    elif M[j, i+1] == 'O':
        push_right(M, (j, i+1), 'O')
    # Part 2
    elif M[j, i+1] == '[' and M[j, i] == '@':  # Robot is right beside box
        push_right(M, (j, i+1), '[')
    elif M[j, i+2] == '[' and M[j, i] == '[':  # Box is right beside box
        push_right(M, (j, i+2), '[')

    if M[j, i+1] == '.' and (M[j, i] == '@' or M[j, i] == 'O'):
        M[j, i+1] = item
        M[j, i] = '.'
    # Part 2
    elif M[j, i+2] == '.' and M[j, i+1] == ']' and M[j, i] == '[':
        M[j, i+2] = ']'
        M[j, i+1] = '['
        M[j, i] = '.'


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_15.txt'

    # Write file contents into matrix
    M = []
    direcs = ''
    with open(filename, "r") as f:
        for line in f:
            if line == '\n':
                pass
            elif len(line) > 100:
                direcs += line.strip()
            else:
                line_list = line.strip()
                M.append(line_list)

    # For Part 2
    N = M.copy()
    M = [list(line) for line in M]
    M = np.array(M, dtype=object)



    # Part 1
    for direc in direcs:
        robot_loc = (np.where(M == '@')[0][0], np.where(M == '@')[1][0])
        # print(direc)
        if direc == '^':
            push_up(M, robot_loc, '@')
        elif direc == 'v':
            push_down(M, robot_loc, '@')
        elif direc == '<':
            push_left(M, robot_loc, '@')
        elif direc == '>':
            push_right(M, robot_loc, '@')
        # print(M)

    boxes_loc = np.where(M == 'O')
    gps_sum = sum([100*j for j in boxes_loc[0]]) + sum([i for i in boxes_loc[1]])
    print('Part 1: ', gps_sum)  # Correct

    # Part 2
    N = [line.replace('#', '##') for line in N]
    N = [line.replace('O', '[]') for line in N]
    N = [line.replace('.', '..') for line in N]
    N = [line.replace('@', '@.') for line in N]
    N = [list(line) for line in N]
    N = np.array(N, dtype=object)

    for direc in direcs:
        robot_loc = (np.where(N == '@')[0][0], np.where(N == '@')[1][0])
        if direc == '^':
            check_move = N.copy()
            push_up(N, robot_loc, '@')  # This moves boxes as long as there is free space above, even if robot didn't move so...
            # Determine if robot did move... if not reset position
            if np.where(check_move == '@') == np.where(N == '@'):
                N = check_move
        elif direc == 'v':
            check_move = N.copy()
            push_down(N, robot_loc, '@')  # Likewise
            if np.where(check_move == '@') == np.where(N == '@'):
                N = check_move
        elif direc == '<':
            push_left(N, robot_loc, '@')
        elif direc == '>':
            push_right(N, robot_loc, '@')

    boxes_loc = np.where(N == '[')
    gps_sum = sum([100*j for j in boxes_loc[0]]) + sum([i for i in boxes_loc[1]])
    print('Part 2: ', gps_sum)  # Correct
