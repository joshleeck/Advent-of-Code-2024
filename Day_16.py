import numpy as np
import heapq


def make_graph_up(M):
    graph = {}
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i] != '#':
                adj = []
                for ele in [(j-1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1))
                for ele in [(j+1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 2001))
                for ele in [(j, i-1), (j, i+1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1001))
                graph[(j, i)] = adj
    return graph


def make_graph_down(M):
    graph = {}
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i] != '#':
                adj = []
                for ele in [(j-1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 2001))
                for ele in [(j+1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1))
                for ele in [(j, i-1), (j, i+1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1001))
                graph[(j, i)] = adj
    return graph


def make_graph_left(M):
    graph = {}
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i] != '#':
                adj = []
                for ele in [(j, i+1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 2001))
                for ele in [(j, i-1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1))
                for ele in [(j+1, i), (j-1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1001))
                graph[(j, i)] = adj
    return graph


def make_graph_right(M):
    graph = {}
    for j in range(M.shape[0]):
        for i in range(M.shape[1]):
            if M[j, i] != '#':
                adj = []
                for ele in [(j, i+1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1))
                for ele in [(j, i-1)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 2001))
                for ele in [(j+1, i), (j-1, i)]:
                    if M[ele] == '.' or M[ele] == 'E':
                        adj.append((ele, 1001))
                graph[(j, i)] = adj
    return graph


def dijkstra(graph_up, graph_down, graph_left, graph_right, start):
    # Dijkstra's algorithm modified to suit the puzzle; edges weights depend on direction

    # Initialize distances from the start node to infinity for all nodes except the start node
    graph_all = graph_up.copy()
    distances = {node: float('infinity') for node in graph_all}  # Using graph_up as template
    distances[start] = 0
    # Priority queue to store nodes for exploration
    pq = [(0, start, None)]  # (distance, current node, parent node)

    while pq:
        # Except for initial face direction, the subsequent face directions are based on last travelled node
        current_distance, current_node, parent_node = heapq.heappop(pq)
        if parent_node is None:
            current_face = (0, 1)
        else:
            current_face = (np.subtract(current_node, parent_node)[0], np.subtract(current_node, parent_node)[1])

        # Skip this node if it has already been processed with a shorter distance
        if current_distance > distances[current_node]:
            continue

        if current_face == (0, 1):
            graph = graph_right.copy()
        elif current_face == (0, -1):
            graph = graph_left.copy()
        elif current_face == (-1, 0):
            graph = graph_up.copy()
        elif current_face == (1, 0):
            graph = graph_down.copy()
        else:
            print('Error in parent node and current node distances')
            break

        for node in graph_all[current_node]:
            # Explore neighbours
            neighbour = node[0]  # Get tuple index
            extracted = [node for node in graph[current_node] if node[0] == neighbour]
            weight = extracted[0][1]  # Get corresponding weight of current node from direction-based graph
            distance = current_distance + weight

            # Only consider this path if it's better than the previously known one
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                parent = current_node
                heapq.heappush(pq, (distance, neighbour, parent))

    return distances


def search_up_fill_corners(M, start):
    j, i = start

    if M[j-1, i] == '.':
        search_up_fill_corners(M, (j-1, i))
    if M[j-1, i] == 'O':
        M[j, i] = 'O'
    else:
        return None


def search_down_fill_corners(M, start):
    j, i = start

    if M[j+1, i] == '.':
        search_down_fill_corners(M, (j+1, i))
    if M[j+1, i] == 'O':
        M[j, i] = 'O'
    else:
        return None


def search_left_fill_corners(M, start):
    j, i = start

    if M[j, i-1] == '.':
        search_left_fill_corners(M, (j, i-1))
    if M[j, i-1] == 'O':
        M[j, i] = 'O'
    else:
        return None


def search_right_fill_corners(M, start):
    j, i = start

    if M[j, i+1] == '.':
        search_right_fill_corners(M, (j, i+1))
    if M[j, i+1] == 'O':
        M[j, i] = 'O'
    else:
        return None


if __name__ == "__main__":
    # Read shared file
    filename = 'C:/Users/User/PycharmProjects/AdventOfCode2024/Data_Day_16.txt'

    # Write file contents into matrix
    M = []
    with open(filename, "r") as f:
        for line in f:
            line_list = list(line.strip())
            M.append(line_list)

    M = np.array(M)

    # Part 1
    start = np.where(M == 'S')[0][0], np.where(M == 'S')[1][0]
    end = np.where(M == 'E')[0][0], np.where(M == 'E')[1][0]

    graph_up = make_graph_up(M)
    graph_down = make_graph_down(M)
    graph_left = make_graph_left(M)
    graph_right = make_graph_right(M)

    shortest_paths = dijkstra(graph_up, graph_down, graph_left, graph_right, start)
    print(shortest_paths[end])  # Correct

    # Part 2
    # Due to the coding approach, need to account for start point having to turn
    best_cost_with_no_turn = shortest_paths[end]
    best_cost_with_S_turn = shortest_paths[end] + 1000
    N = M.copy()
    N[M == 'S'] = 'E'
    N[M == 'E'] = 'S'
    graph_up = make_graph_up(N)
    graph_down = make_graph_down(N)
    graph_left = make_graph_left(N)
    graph_right = make_graph_right(N)

    # Run algorithm backwards from the end
    start = np.where(N == 'S')[0][0], np.where(N == 'S')[1][0]
    end = np.where(N == 'E')[0][0], np.where(N == 'E')[1][0]
    shortest_paths_opp = dijkstra(graph_up, graph_down, graph_left, graph_right, start)
    track = set()
    for key in shortest_paths.keys():
        j, i = key
        if shortest_paths[(j, i)] + shortest_paths_opp[(j, i)] == best_cost_with_S_turn:
            track.add((j, i))
        if shortest_paths[(j, i)] + shortest_paths_opp[(j, i)] == best_cost_with_no_turn:
            track.add((j, i))

    # For visualisation to debug
    for index in track:
        M[index] = 'O'

    for index in track:
        j, i = index
        search_up_fill_corners(M, (j, i))
        search_down_fill_corners(M, (j, i))
        search_left_fill_corners(M, (j, i))
        search_right_fill_corners(M, (j, i))

    for j in range(M.shape[0]):
        print(list(M[j, :]))

    print(len(np.where(M == 'O')[0]))  # Correct
