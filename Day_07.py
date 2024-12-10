def operate(pos_oper, val_list, next_num):
    new_nums = []
    for val in val_list:
        for oper in pos_oper:
            if oper == 0:
                new_nums.append(val + next_num)
            if oper == 1:
                new_nums.append(val * next_num)
            if oper == 2:
                new_nums.append(int(str(val) + str(next_num)))
    return new_nums

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_07.txt'

    # Write file contents into matrix
    test_values = []
    nums = []
    with open(filename, "r") as f:
        for line in f:
            equation = list(line.strip().split(':'))
            test_value = equation[0]
            num = equation[1].strip().split(' ')
            test_values.append(test_value)
            nums.append(num)

    # Part 1
    pos_oper = [0, 1] #  +, x
    sum = 0
    for i in range(len(test_values)):
        test_value = int(test_values[i])
        all_pos_values = []
        numbers = [int(num) for num in nums[i]]
        val = numbers[0]
        print(numbers)
        val_tmp = [val]
        for i in range(1, len(numbers)):
            val_tmp = operate(pos_oper, val_tmp, numbers[i])
            if i == len(numbers)-1: all_pos_values = val_tmp

        if test_value in all_pos_values:
            print('Calibrated')
            sum += test_value

    print(sum)  # Correct

    # Part 2
    pos_oper = [0, 1, 2]  # +, x, ||
    sum = 0
    for i in range(len(test_values)):
        test_value = int(test_values[i])
        all_pos_values = []
        numbers = [int(num) for num in nums[i]]
        val = numbers[0]
        print(numbers)
        val_tmp = [val]
        for i in range(1, len(numbers)):
            val_tmp = operate(pos_oper, val_tmp, numbers[i])
            if i == len(numbers)-1: all_pos_values = val_tmp

        if test_value in all_pos_values:
            print('Calibrated')
            sum += test_value

    print(sum)  # Correct
