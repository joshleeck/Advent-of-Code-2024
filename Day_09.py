if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_09.txt'

    with open(filename, "r") as f:
        diskmap = f.readline()

    #print(diskmap)

    # Part 1
    expanded_disk = []
    arr = list(diskmap)
    # Expand disk according to rules
    ind = 0
    for i in range(len(arr)):
        if i%2 == 0:
            expanded_disk += [str(ind)]*int(arr[i])
            ind += 1
        else:
            expanded_disk += ['.']*int(arr[i])

    # Keep moving until no more '.' spaces
    while True:
        try:
            next_slot = expanded_disk.index('.')
        except:
            break
        expanded_disk[next_slot] = expanded_disk[-1]
        expanded_disk = expanded_disk[:-1]

    #print(expanded_disk)
    
    # Compute sum following instructions
    sum = 0
    for i, num in enumerate(expanded_disk):
        sum += i*int(num)

    print(sum)  # Correct


    # Part 2
    expanded_disk = []
    arr = list(diskmap)
    # Expand disk according to rules
    ind = 0
    ind_d = {}
    for i in range(len(arr)):
        if i % 2 == 0:
            expanded_disk += [str(ind)] * int(arr[i])
            ind_d[str(ind)] = int(arr[i])
            ind += 1
        else:
            expanded_disk += ['.'] * int(arr[i])

    for i in reversed(range(1, ind)):
        print(i)
        chunk_st = expanded_disk.index(str(i))
        chunk = expanded_disk[chunk_st:chunk_st+ind_d[str(i)]]
        mem_gap = ['.'] * len(chunk)
        res = [expanded_disk[idx: idx + len(mem_gap)] == mem_gap for idx in range(len(expanded_disk) - len(mem_gap) + 1)]
        try:
            next_slot = res.index(True)
            if next_slot < chunk_st:  # Make sure not moving memory further into string
                expanded_disk[next_slot:next_slot + len(chunk)] = expanded_disk[chunk_st:chunk_st + ind_d[str(i)]]
                expanded_disk[chunk_st:chunk_st + ind_d[str(i)]] = mem_gap
        except:
            continue

    # Compute sum following instructions
    sum = 0
    for i, num in enumerate(expanded_disk):
        if num != '.':
            sum += i * int(num)

    print(sum)  # Correct




