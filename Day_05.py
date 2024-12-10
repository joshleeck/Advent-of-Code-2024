import math
import numpy as np

def check_update(update, rule_book):
    passed = True
    for rule in rule_book:
        a = rule[0];
        b = rule[1]
        if a in update and b in update:
            if update.index(a) > update.index(b):
                passed = False
    return passed


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_05.txt'

    rule_book = []
    update_list = []
    sec2 = False
    with open (filename, "r") as f:
        for line in f:
            line_list = line.strip()
            if line_list == '':
                sec2 = True
                continue
            if not sec2:
                rule_book.append(line_list.split('|'))
            else:
                update_list.append(line_list.split(','))

    # Part 1
    rule_book = sorted(rule_book)
    update_pass = []
    for update in update_list:
        if check_update(update, rule_book):
            update_pass.append(update)

    sum = 0
    for update in update_pass:
        sum += int(update[(math.floor(len(update)/2.))])

    print('Part 1:', sum)  # Correct

    # Part 2
    update_nopass = [update for update in update_list if update not in update_pass]
    #print(len(update_nopass))

    # Fix the update
    fixed_update = []
    for update in update_nopass:
        print('Fixing: ', update)
        rule_book_portion = [rule for rule in rule_book if rule[0] in update and rule[1] in update]
        # After filtering rules, all updates have the full relationships to order the numbers based on appearances
        arr = np.array(rule_book_portion)[:, 1]
        d = {}
        for num in update:
            d[num] = np.sum(arr == num)
        keys = list(d.keys())
        values = list(d.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        fixed = list(sorted_dict)
        print('Fixed: ', fixed)
        fixed_update.append(fixed)

    sum = 0
    for update in fixed_update:
        sum += int(update[(math.floor(len(update)/2.))])

    print('Part 2:', sum)  # Correct
