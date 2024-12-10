if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_01.txt'

    with open(filename) as file:
        list_a = []
        list_b = []
        for line in file:
            data_line = line.rstrip().split(' ')
            list_a.append(int(data_line[0]))
            list_b.append(int(data_line[3]))

    # Part 1
    list_a = sorted(list_a)
    list_b = sorted(list_b)

    diff_sum = 0
    for i in range(len(list_a)):
        diff_sum += abs(list_a[i] - list_b[i])

    print(diff_sum)  # Correct

    # Part 2
    sim_sum = 0
    for i in range(len(list_a)):
        sim_sum += list_a[i] * list_b.count(list_a[i])

    print(sim_sum)  # Correct

