import itertools
import numpy as np


def is_close(a, b, err_tol):
    if abs(a - b) <= err_tol:
        return a
    return b


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_13.txt'

    setups = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
        spl = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '') if not x]
        for setup in spl:
            A_x = setup[0].split(':')[-1].split(',')[0].split('+')[-1]
            A_y = setup[0].split(':')[-1].split(',')[1].split('+')[-1]
            B_x = setup[1].split(':')[-1].split(',')[0].split('+')[-1]
            B_y = setup[1].split(':')[-1].split(',')[1].split('+')[-1]
            prize_x = setup[2].split(':')[-1].split(',')[0].split('=')[-1]
            prize_y = setup[2].split(':')[-1].split(',')[1].split('=')[-1]
            simul = [[int(A_x), int(B_x)], [int(A_y), int(B_y)], [int(prize_x), int(prize_y)]]
            setups.append(simul)

    # Part 1
    tokens_a = 3
    tokens_b = 1
    sum_tokens = 0
    for simul in setups:
        res = np.linalg.inv([simul[0], simul[1]]).dot(simul[2])
        res_a = is_close(round(res[0]), res[0], 1e-7)  # Allowing for precision errors
        res_b = is_close(round(res[1]), res[1], 1e-7)
        if res_a%1 == 0 and res_b%1 == 0:  # Check if whole numbers
            print(res_a, res_b)
            sum_tokens += tokens_a * res_a + tokens_b * res_b
        else:
            print('No possible combination')

    print(sum_tokens)  # Correct

    # Part 2
    tokens_a = 3
    tokens_b = 1
    sum_tokens = 0
    for simul in setups:
        prize_loc = [x + 10000000000000 for x in simul[2]]
        res = np.linalg.inv([simul[0], simul[1]]).dot(prize_loc)
        print(res)
        res_a = is_close(round(res[0]), res[0], 1e-4)  # Allowing for precision errors
        res_b = is_close(round(res[1]), res[1], 1e-4)
        if res_a%1 == 0 and res_b%1 == 0:  # Check if whole numbers
            print(res_a, res_b)
            sum_tokens += tokens_a * res_a + tokens_b * res_b
        else:
            print('No possible combination')

    print(sum_tokens)  # Correct

