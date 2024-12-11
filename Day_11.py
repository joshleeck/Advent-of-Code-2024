import functools

def update_stone(stone, blinks):
    stone = int(stone)
    digits = len(str(stone))
    stone = str(stone)
    if blinks == 0:
        return 1
    if stone == '0':
        return update_stone('1', blinks - 1)
    elif len(str(stone))%2 == 0:
        stone_a = stone[:int(digits/2)]
        stone_b = stone[int(digits/2):]
        return update_stone(stone_a, blinks - 1) + update_stone(stone_b, blinks - 1)
    else:
        return update_stone(str(int(stone)*2024), blinks - 1)

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_11.txt'

    with open(filename, "r") as f:
        stones = f.readline().split(' ')

    # Part 1
    stone_list = [int(x) for x in stones]
    count = 0
    for stone in stone_list:
        count += update_stone(stone, 25)

    print(count)  # Correct


    # Part 2
    stone_list = [int(x) for x in stones]

    # Need to speed up so cache the function's output
    update_stone = functools.cache(update_stone)

    count = 0
    for stone in stone_list:
        print(stone)
        count += update_stone(stone, 75)

    print(count)  # Correct