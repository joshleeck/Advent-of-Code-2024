import numpy as np

if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_08.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    # Clone array for Part 2
    M = np.array(M)
    N = np.empty([M.shape[0], M.shape[1]], dtype="str")
    N[:,:] = '!'

    # Node list
    nums = ['0','1','2','3','4','5','6','7','8','9']
    nl_low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    nl_upp = [alph.upper() for alph in nl_low]
    nl = nl_low + nl_upp + nums

    # Part 1
    for alphnum in nl:
        indices = zip(*np.where(M == alphnum))
        coord_list = []
        for j, i in indices:
            coord_list.append((j,i))
        for coord in coord_list:
            other_coord = coord_list.copy()
            other_coord.remove(coord)
            for o_coord in other_coord:
                diff = tuple(np.subtract(o_coord, coord))
                backw = tuple(np.subtract(coord, diff))
                forw = tuple(np.add(o_coord, diff))  # Add diff on other coord
                obb = [backw[0] < 0, backw[0] > M.shape[0]-1, backw[1] < 0, backw[1] > M.shape[1]-1]
                obf = [forw[0] < 0, forw[0] > M.shape[0]-1, forw[1] < 0, forw[1] > M.shape[1]-1]
                if not any(obb):
                    #print(backw)
                    N[backw] = '#'
                if not any(obf):
                    #print(forw)
                    N[forw] = '#'

    print('Part 1: ', np.sum(N == '#'))  # Correct

    # Part 2
    for alphnum in nl:
        indices = zip(*np.where(M == alphnum))
        coord_list = []
        for j, i in indices:
            coord_list.append((j,i))
        for coord in coord_list:
            other_coord = coord_list.copy()
            other_coord.remove(coord)
            for o_coord in other_coord:
                for mult in range(0,max(N.shape[0],N.shape[1])):  # In Part 2, just need to loop through multiplier
                    diff = tuple(np.subtract(o_coord, coord))
                    diff = tuple(np.multiply(diff, mult))  # Additional step
                    backw = tuple(np.subtract(coord, diff))
                    forw = tuple(np.add(o_coord, diff))  # Add diff on other coord
                    obb = [backw[0] < 0, backw[0] > M.shape[0]-1, backw[1] < 0, backw[1] > M.shape[1]-1]
                    obf = [forw[0] < 0, forw[0] > M.shape[0]-1, forw[1] < 0, forw[1] > M.shape[1]-1]
                    if not any(obb):
                        #print(backw)
                        N[backw] = '#'
                    if not any(obf):
                        #print(forw)
                        N[forw] = '#'

    print('Part 2: ', np.sum(N == '#'))  # Correct


