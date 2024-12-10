import re
import copy

def mul(x, y):
    return x * y

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_03.txt'

    with open(filename) as file:
        memory_str = file.read().replace('\n', '')

    memory_str2 = copy.copy(memory_str)  # For Part 2

    # Part 1
    filtered = []
    max_digits = 3
    pattern = 'mul('  # Brute force matching
    # Start with minimum 1 digits, maximum 3 digits
    while pattern in memory_str:
        x = memory_str.index(pattern)
        found = False
        for dig1 in range(1, max_digits+1):
            for dig2 in range(1, max_digits+1):
                # Hard check for pattern match
                if memory_str[x + 4 + dig1] == ',' and memory_str[x + 4 + dig1 + dig2 + 1] == ')':
                    #print(memory_str[x:x + 4 + dig1 + dig2 + 2])
                    filtered.append(memory_str[x:x + 4 + dig1 + dig2 + 2])
                    memory_str = memory_str[x+1:]  # Shorten string by x+1 character
                    found = True
        if not found:  # Handle instances when match not found, shorten string by 1 character
            memory_str = memory_str[1:]

    sum = 0
    for i in range(len(filtered)):
        a, b = list(map(int, re.findall(r'\d+', filtered[i])))
        sum += mul(a, b)
    print('Part 1: ', sum)

    # Part 2
    filtered = []
    max_digits = 3
    pattern = "mul("  # Brute force matching
    yes_flag = "do()"
    no_flag = "don't()"
    do = True
    while pattern in memory_str2:
        x = memory_str2.index(pattern)
        try:
            y = memory_str2.index(yes_flag)
        except:
            y = 100000  # Initialise very large value since no more future occurrences
        try:
            z = memory_str2.index(no_flag)
        except:
            z = 100000  # Initialise very large value since no more future occurrences
        if z < x < y:  # Don't flag has occurred before the next mul and do flag
            do = False
            memory_str2 = memory_str2[z+1:]  # Cut to the don't flag and continue
            continue
        if y < x < z:  # Do flag has occurred before the next mul and don't flag
            do = True
            memory_str2 = memory_str2[y+1:]  # Cut to the do flag and continue
            continue
        # Start with minimum 1 digits, maximum 3 digits
        if do:
            found = False
            for dig1 in range(1, max_digits+1):
                for dig2 in range(1, max_digits+1):
                    # Hard check for pattern match
                    if memory_str2[x + 4 + dig1] == ',' and memory_str2[x + 4 + dig1 + dig2 + 1] == ')':
                        #print(memory_str2[x:x + 4 + dig1 + dig2 + 2])
                        filtered.append(memory_str2[x:x + 4 + dig1 + dig2 + 2])
                        memory_str2 = memory_str2[x+1:]  # Shorten string by x+1 character
                        found = True
            if not found:  # Handle instances when match not found, shorten string by 1 character
                memory_str2 = memory_str2[1:]
        else:
            memory_str2 = memory_str2[1:]

    sum = 0
    for i in range(len(filtered)):
        a, b = list(map(int, re.findall(r'\d+', filtered[i])))
        sum += mul(a, b)
    print('Part 2: ', sum)

