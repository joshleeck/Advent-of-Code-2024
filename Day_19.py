from collections import deque
from functools import cache

# Without using caching
def check_design(design, towels):
    # Initial slice options
    max_len = max([len(towel) for towel in towels])
    min_len = min([len(towel) for towel in towels])
    slice_opts = [design[:slice_len] for slice_len in range(min_len, max_len+1)]
    rep = [sli for sli in slice_opts if sli in towels]  # Only keep those subslice that are in towels
    rep = sorted(rep)[::-1]  # Start with longest chunks
    rep = list(set(rep))
    queue = deque()
    for items in rep:
        queue.append(items)

    seen = []
    while not len(queue) == 0:
        slice = queue.popleft()  # Dequeue first slice
        if slice == design:
            return True

        crop = len(slice)
        slice_opts = [design[crop:crop + slice_len] for slice_len in range(min_len, max_len+1)]
        rep = [sli for sli in slice_opts if sli in towels]  # Only keep those subslice that are in towels
        rep = sorted(rep)[::-1]  # Start with longest chunks
        rep = list(set(rep))
        if rep:
            rep = [slice + sli for sli in rep]  # Prepend full slice to subslice
            for items in rep:
                if items not in seen:
                    queue.appendleft(items)  # Enqueue the new slices in front of queue to speed processing
                    seen.append(items)


# With caching by HyperNeutrino Youtube, brute force
@cache
def check_unique_design(design, towels):
    max_len = max([len(towel) for towel in towels])
    if design == "":
        return 1
    count = 0
    for i in range(min(len(design), max_len) + 1):
        if design[:i] in towels:
            count += check_unique_design(design[i:], towels)
    return count


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_19.txt'

    designs = []
    with open(filename, "r") as f:
        for line in f:
            if len(line) > 100:
                towels = line.strip().split(', ')
            elif line.strip():
                designs.append(line.strip())

    # Part 1
    count = 0
    design_pass = []
    for design in designs:
        if check_design(design, towels):
            design_pass.append(design)
            count += 1

    print(count)  # Correct

    # Part 2
    unique = 0
    for design in design_pass:
        towels = tuple(towels)
        unique += check_unique_design(design, towels)

    print(unique)  # Correct
