def check_good(report_levels):
    # Report is fully ascending or descending
    if (sorted(report_levels) == report_levels) or (sorted(report_levels, reverse=True) == report_levels):
        good_flag = True
        for i in range(1, len(report_levels)):
            diff = report_levels[i] - report_levels[i - 1]
            # Check differences are within criteria
            if abs(diff) > 3 or abs(diff) < 1:
                return False
    # Report is not fully ascending or descending
    else:
        good_flag = False
    return good_flag


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_02.txt'

    with open(filename) as file:
        report_list = [line.rstrip() for line in file]

    # Part 1
    count = 0
    for report in report_list:
        levels = report.split(' ')
        levels = [int(level) for level in levels]

        good = check_good(levels)
        if good:
            count += 1

    print("Part 1: ", count)  # Correct

    # Part 2
    count_damp = 0
    for report in report_list:
        levels = report.split(' ')
        levels = [int(level) for level in levels]

        good = check_good(levels)
        # Check bad reports if damping resolves it
        if not good:
            for i in range(len(levels)):
                levels_copy = levels.copy()
                levels_copy.pop(i)
                if check_good(levels_copy):
                    good = True
                    count_damp += 1
                    break

    print("Part 2: ", count_damp)  # Correct
