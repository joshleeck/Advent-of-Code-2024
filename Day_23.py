import networkx as nx


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_23.txt'

    # Write file contents into matrix
    conn_list = []
    with open(filename, "r") as f:
        for line in f:
            line_list = line.strip()
            conn_list.append(line_list)

    # Part 1
    conn_dict = {}
    for conn in conn_list:
        a, b = conn.split('-')
        if a not in conn_dict.keys():
            conn_dict[a] = set()
            conn_dict[a].add(b)
        else:
            conn_dict[a].add(b)
        if b not in conn_dict.keys():
            conn_dict[b] = set()
            conn_dict[b].add(a)
        else:
            conn_dict[b].add(a)

    lan = []
    for item in conn_dict.keys():
        # Get item connections
        connections = conn_dict[item]
        # Check other connections within item connections
        for connection1 in connections:
            # If there is a connection between any of the other connections, it means 3 are connected
            for connection2 in connections:
                if connection2 in conn_dict[connection1]:
                    if {item, connection1, connection2} not in lan:
                        lan.append({item, connection1, connection2})

    count = 0
    lan_update = []
    for lan_i in lan:
        if any(x[0] == 't' for x in lan_i):
            lan_update.append(lan_i)
            count += 1

    print(count)  # Correct

    # Part 2
    g = nx.Graph()
    # Re-building graph from initial list
    for conn in conn_list:
        a, b = conn.split('-')
        g.add_edge(a, b)
        g.add_edge(b, a)

    max_clique_size = 0
    # Find all cliques
    cliques = nx.find_cliques(g)
    for clique in cliques:
        if len(clique) >= max_clique_size:
            max_clique_size = len(clique)
            max_clique = clique

    max_clique = sorted(max_clique)
    print(','.join(max_clique))  # Correct

