import numpy as np

def add_trailsteps(M, trail):
    j = trail[-1][0]
    i = trail[-1][1]
    cur_num = M[j, i]
    next_num = str(int(cur_num) + 1)

    fork1 = trail.copy()
    fork2 = trail.copy()
    fork3 = trail.copy()
    fork4 = trail.copy()

    if j+1 <= M.shape[0]-1:
        if M[j+1, i] == next_num:
            fork1.append((j+1, i))
        else:
            fork1.append('deadend')
    else:  # Out of bounds
        fork1.append('deadend')

    if j-1 >= 0:
        if M[j-1, i] == next_num:
            fork2.append((j-1, i))
        else:
            fork2.append('deadend')
    else:  # Out of bounds
        fork2.append('deadend')

    if i+1 <= M.shape[1]-1:
        if M[j, i+1] == next_num:
            fork3.append((j, i+1))
        else:
            fork3.append('deadend')
    else:  # Out of bounds
        fork3.append('deadend')

    if i-1 >= 0:
        if M[j, i-1] == next_num:
            fork4.append((j, i-1))
        else:
            fork4.append('deadend')
    else:  # Out of bounds
        fork4.append('deadend')

    return fork1, fork2, fork3, fork4

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_10.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    M = np.array(M)

    # Part 1
    indices = zip(*np.where(M == '0'))
    trailheads = []
    for j, i in indices:
        trailheads.append((j, i))

    leads_to_peak = {}
    # Start grid search
    all_trails = []
    for trailhead in trailheads:
        end_trails = []
        for i in range(0, 9):
            if i == 0:
                updated_trails = [[trailhead]]
            else:
                updated_trails = end_trails.copy()
            for trail in updated_trails:
                f1, f2, f3, f4 = add_trailsteps(M, trail)
                # Keep only the forks which continue
                # print([f1, f2, f3, f4])
                new_trails = [fork for fork in [f1, f2, f3, f4] if 'deadend' not in fork]
                end_trails += new_trails
                end_trails = [fork for fork in end_trails if len(fork) == i + 2]

        # Only include the head and end, and avoid duplication
        for x in end_trails:
            head_end = (x[0], x[-1])
            if head_end not in all_trails:
                all_trails.append(head_end)

    print('Part 1: ', len(all_trails))  # Correct

    # Part 2
    indices = zip(*np.where(M == '0'))
    trailheads = []
    for j, i in indices:
        trailheads.append((j, i))

    leads_to_peak = {}
    # Start grid search
    all_trails = []
    for trailhead in trailheads:
        end_trails = []
        for i in range(0,9):
            if i == 0:
                updated_trails = [[trailhead]]
            else:
                updated_trails = end_trails.copy()
            for trail in updated_trails:
                f1, f2, f3, f4 = add_trailsteps(M, trail)
                # Keep only the forks which continue
                #print([f1, f2, f3, f4])
                new_trails = [fork for fork in [f1, f2, f3, f4] if 'deadend' not in fork]
                end_trails += new_trails
                # Remove old forks to ensure current path length is correct (after 0th iteration, path length is 2)
                end_trails = [fork for fork in end_trails if len(fork) == i+2]

        all_trails += end_trails

    print('Part 2: ', len(all_trails))  # Correct
