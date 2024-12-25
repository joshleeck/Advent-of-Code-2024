def trace_origin(end, conn_list):
    for conn in conn_list:
        if end in conn[1]:
            print(conn)


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_24.txt'

    # Write file contents into lists
    init_wire = []
    conn_list = []
    with open(filename, "r") as f:
        for line in f:
            if "->" not in line.strip() and line.strip():
                wire, val = line.strip().split(':')
                init_wire.append((wire.strip(), int(val.strip())))
            elif not line.strip():
                pass
            else:
                conn, wire_out = line.strip().split('->')
                conn_list.append((conn.strip(), wire_out.strip()))

    # Part 1
    wire_dict = {}
    for wire in init_wire:
        wire_dict[wire[0]] = wire[1]

    to_do = conn_list.copy()
    while to_do:
        for conn in to_do:
            wire_a, oper, wire_b = conn[0].split(' ')
            try:
                if oper == 'AND':
                    wire_dict[conn[1]] = wire_dict[wire_a] & wire_dict[wire_b]
                elif oper == 'OR':
                    wire_dict[conn[1]] = wire_dict[wire_a] | wire_dict[wire_b]
                elif oper == 'XOR':
                    wire_dict[conn[1]] = wire_dict[wire_a] ^ wire_dict[wire_b]
                to_do.remove(conn)
            except:
                pass

    z_list = [(z, wire_dict[z]) for z in wire_dict.keys() if z[0] == 'z']

    z_list = sorted(z_list, reverse=True)
    zstr_list = [str(z[1]) for z in z_list]
    zstr = ''.join(zstr_list)
    bin_zstr = int(zstr, 2)
    print(bin_zstr)  # Correct

    # Part 2
    inputs = [conn[0].split(' ') for conn in conn_list]
    outputs = [conn[1] for conn in conn_list]

    trace_origin('tvp', conn_list)
    trace_origin('z15', conn_list)
    trace_origin('fsh', conn_list)
    trace_origin('dcr', conn_list)
    trace_origin('vdk', conn_list)
    trace_origin('mmf', conn_list)
    trace_origin('z25', conn_list)
    trace_origin('dpg', conn_list)
    trace_origin('z10', conn_list)
    trace_origin('kmb', conn_list)

    # For tracing problematic bits
    for num in range(45):
        # Reset wire dictionary
        wire_dict = {}
        for wire in init_wire:
            wire_dict[wire[0]] = wire[1]

        suffix = str(num).zfill(2)
        for key in wire_dict.keys():
            if key == 'x' + suffix or key == 'y' + suffix:
                wire_dict[key] = 1
            else:
                wire_dict[key] = 0

        inps = inputs.copy()
        outs = outputs.copy()

        # First swap to deal with z15
        # swap1, swap2 = outs.index('fsh'), outs.index('dcr')
        # outs[swap1], outs[swap2] = outs[swap2], outs[swap1]
        swap1, swap2 = outs.index('tvp'), outs.index('z15')
        outs[swap1], outs[swap2] = outs[swap2], outs[swap1]
        # I noticed the solution is non-unique...

        # Second swap to deal with z35
        swap1, swap2 = outs.index('vdk'), outs.index('mmf')
        outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

        # Third swap to deal with z25
        swap1, swap2 = outs.index('z25'), outs.index('dpg')
        outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

        # Last swap to deal with z09
        swap1, swap2 = outs.index('z10'), outs.index('kmb')
        outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

        while inps:
            for i, inp in enumerate(inps):
                wire_a, oper, wire_b = inp
                if wire_a in wire_dict.keys() and wire_b in wire_dict.keys():
                    if oper == 'AND':
                        wire_dict[outs[i]] = wire_dict[wire_a] & wire_dict[wire_b]
                    elif oper == 'OR':
                        wire_dict[outs[i]] = wire_dict[wire_a] | wire_dict[wire_b]
                    elif oper == 'XOR':
                        wire_dict[outs[i]] = wire_dict[wire_a] ^ wire_dict[wire_b]
                    inps.remove(inp)
                    outs.remove(outs[i])

        x_list_cor = []
        y_list_cor = []
        z_list_test = []
        for wire in sorted(wire_dict.keys()):
            if wire[0] == 'x':
                x_list_cor.append(wire_dict[wire])
            elif wire[0] == 'y':
                y_list_cor.append(wire_dict[wire])
            elif wire[0] == 'z':
                z_list_test.append(wire_dict[wire])

        x = ''.join([str(x) for x in x_list_cor])[::-1]
        y = ''.join([str(y) for y in y_list_cor])[::-1]
        z_list_cor = list(bin(int(x, 2) + int(y, 2)))[2:][::-1]
        z_list_cor = [int(z) for z in z_list_cor]

        if z_list_test[:num+2] != z_list_cor[:num+2]:
            print(x_list_cor)
            print(y_list_cor)
            print(z_list_test)
            print(z_list_cor)
            print(num)  # Should have nothing here if all works

    # Test on actual data
    # Reset wire dictionary
    wire_dict = {}
    for wire in init_wire:
        wire_dict[wire[0]] = wire[1]

    inps = inputs.copy()
    outs = outputs.copy()

    # First swap to deal with z15
    # swap1, swap2 = outs.index('fsh'), outs.index('dcr')
    # outs[swap1], outs[swap2] = outs[swap2], outs[swap1]
    swap1, swap2 = outs.index('tvp'), outs.index('z15')
    outs[swap1], outs[swap2] = outs[swap2], outs[swap1]
    # I noticed the solution is non-unique...

    # Second swap to deal with z35
    swap1, swap2 = outs.index('vdk'), outs.index('mmf')
    outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

    # Third swap to deal with z25
    swap1, swap2 = outs.index('z25'), outs.index('dpg')
    outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

    # Last swap to deal with z09
    swap1, swap2 = outs.index('z10'), outs.index('kmb')
    outs[swap1], outs[swap2] = outs[swap2], outs[swap1]

    while inps:
        for i, inp in enumerate(inps):
            wire_a, oper, wire_b = inp
            if wire_a in wire_dict.keys() and wire_b in wire_dict.keys():
                if oper == 'AND':
                    wire_dict[outs[i]] = wire_dict[wire_a] & wire_dict[wire_b]
                elif oper == 'OR':
                    wire_dict[outs[i]] = wire_dict[wire_a] | wire_dict[wire_b]
                elif oper == 'XOR':
                    wire_dict[outs[i]] = wire_dict[wire_a] ^ wire_dict[wire_b]
                inps.remove(inp)
                outs.remove(outs[i])

    x_list_cor = []
    y_list_cor = []
    z_list_test = []
    for wire in sorted(wire_dict.keys()):
        # if num == 2:
        #     print(wire, wire_dict[wire])
        if wire[0] == 'x':
            x_list_cor.append(wire_dict[wire])
        elif wire[0] == 'y':
            y_list_cor.append(wire_dict[wire])
        elif wire[0] == 'z':
            z_list_test.append(wire_dict[wire])


    x = ''.join([str(x) for x in x_list_cor])[::-1]
    y = ''.join([str(y) for y in y_list_cor])[::-1]
    z_list_cor = list(bin(int(x, 2) + int(y, 2)))[2:][::-1]
    z_list_cor = [int(z) for z in z_list_cor]
    z = ''.join([str(z) for z in z_list_cor])[::-1]

    print(x_list_cor)
    print(y_list_cor)
    print(z_list_test)
    print(z_list_cor)

    if int(x, 2) + int(y, 2) == int(z, 2):
        print('Success')

    # Copied from above
    swaps = ['tvp','z15','vdk','mmf','z25','dpg','z10','kmb']
    swaps = sorted(swaps)
    print(','.join(swaps))  # Correct
