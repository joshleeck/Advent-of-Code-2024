import math
import copy


def adv(A, operand):
    frac = A/(2**operand)
    A = math.trunc(frac)
    return A


def bxl(B, operand):
    B = B ^ operand
    return B


def bst(operand):
    B = operand % 8
    return B


def jnz(A, inst, operand):
    if A == 0:
        pass
        return inst, True
    else:
        return operand, False


def bxc(B, C):
    B = B ^ C
    return B


def out(std, operand):
    std.append(operand % 8)


def bdv(A, operand):
    frac = A/(2**operand)
    B = math.trunc(frac)
    return B


def cdv(A, operand):
    frac = A/(2**operand)
    C = math.trunc(frac)
    return C


def hash(input):
    A = input[0]
    B = input[1]
    C = input[2]
    inst = 0  # Instruction index
    std = []  # Output store
    while inst < len(prog):
        opcode = int(prog[inst])
        operand_l = int(prog[inst + 1])

        if operand_l == 4:
            operand = copy.copy(A)
        elif operand_l == 5:
            operand = copy.copy(B)
        elif operand_l == 6:
            operand = copy.copy(C)
        else:
            operand = operand_l

        if opcode == 0:
            A = adv(A, operand)
        elif opcode == 1:
            B = bxl(B, operand_l)
        elif opcode == 2:
            B = bst(operand)
        elif opcode == 3:
            inst, skip = jnz(A, inst, operand)
        elif opcode == 4:
            B = bxc(B, C)
        elif opcode == 5:
            out(std, operand)
        elif opcode == 6:
            B = bdv(A, operand)
        elif opcode == 7:
            C = cdv(A, operand)

        if opcode == 3:
            if skip:
                inst += 2
            else:
                pass
        else:
            inst += 2

    return std


def check_output(input, prog):
    std = hash(input, prog)
    if std != prog:
        return False
    return True


# Back engineer from my prog: 2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0
# b = a % 8
# b = b ^ 1
# c = a >> b
# b = b ^ c
# b = b ^ 4
# a = a >> 3    # This line can effectively be brought above and reverse >> to <<
# out(b % 8)
# if a != 0, jump 0
def find(prog, ans):
    if not prog:
        return ans
    for b in range(8):
        a = ans << 3 | b
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ c
        b = b ^ 4
        if b % 8 == prog[-1]:
            sub = find(prog[:-1], a)
            if sub is None:
                continue
            return sub


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_17.txt'

    with open(filename, "r") as f:
        A = int(f.readline().split(': ')[-1])
        B = int(f.readline().split(': ')[-1])
        C = int(f.readline().split(': ')[-1])
        f.readline()
        prog = list(f.readline().split(': ')[-1].split(','))

    # Part 1
    input = (A, B, C)
    std = hash(input)
    print(",".join([str(i) for i in std]))  # Correct

    # Part 2
    input = (A, B, C)
    prog = [int(i) for i in prog]

    # I had tried to back engineer with inverse ^ and % etc., but didn't know the << and >> trick
    # I had tried brute force and waited for an eternity
    # Learnt from HyperNeutrino Youtube
    # Back engineer my prog: 2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0 (above)
    print(find(prog, 0))  # Correct
