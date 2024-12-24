import math
import sys
import copy
sys.setrecursionlimit(3000)


def update_sec_num(sec_num, iter):
    if iter == 0:
        return sec_num

    else:
        res = sec_num * 64
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216

        res = math.floor(sec_num / 32)
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216

        res = sec_num * 2048
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216
        return update_sec_num(sec_num, iter-1)


def get_sec_num_ones(sec_num, iter, sec_num_ones, sec_num_diff):
    if iter == 0:
        sec_num_diff.append(str(sec_num)[-1])
        return None

    else:
        ori = copy.copy(sec_num)
        res = sec_num * 64
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216

        res = math.floor(sec_num / 32)
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216

        res = sec_num * 2048
        sec_num = res ^ sec_num
        sec_num = sec_num % 16777216

        sec_num_diff.append(int(str(sec_num)[-1]) - int(str(ori)[-1]))
        sec_num_ones.append(str(sec_num)[-1])
        return get_sec_num_ones(sec_num, iter-1, sec_num_ones, sec_num_diff)


def contains_sublist(lst, sublst):
    n = len(sublst)
    seq_found = [(sublst == lst[i:i+n]) for i in range(len(lst)-n+1)]
    if any(seq_found):
        return seq_found.index(True)
    return None


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_22.txt'

    # Write file contents into matrix
    sec_num_list = []
    with open(filename, "r") as f:
        for line in f:
            line_list = line.strip()
            sec_num_list.append(line_list)

    # Part 1
    sec_num_list = [int(x) for x in sec_num_list]
    sum = 0
    for sec_num in sec_num_list:
        sum += update_sec_num(sec_num, 2000)

    print(sum)  # Correct

    # Part 2
    sec_num_list = [int(x) for x in sec_num_list]

    sum = 0
    sec_num_ones_dict = {}
    sec_num_diff_dict = {}
    for sec_num in sec_num_list:
        sec_num_ones = []
        sec_num_diff = []
        get_sec_num_ones(sec_num, 2000, sec_num_ones, sec_num_diff)
        sec_num_ones_dict[sec_num] = sec_num_ones
        sec_num_diff_dict[sec_num] = sec_num_diff

    # Conduct brute force search in subspace
    max_sum = 0
    for a in range(-3,5):
        for b in range(-3,5):
            for c in range(-3,5):
                for d in range(-3,5):
                    sublist = [a, b, c, d]
                    print(sublist)
                    sum = 0
                    for sec_num in sec_num_list:
                        if contains_sublist(sec_num_diff_dict[sec_num], sublist):
                            sum += int(sec_num_ones_dict[sec_num][contains_sublist(sec_num_diff_dict[sec_num], sublist)+3])
                        else:
                            pass

                    print(sum)
                    if sum >= max_sum:
                        max_sum = sum

    print(max_sum)  # Correct
