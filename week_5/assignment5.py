def load_file(file_to_open):
    # load file into a adjacency list
    file = open(file_to_open)
    lines = file.read().split('\n')
    graph = {};
    for line in lines[:-1]: # file ends with extra line break
        row = line.split("\t")
        node = int(row.pop(0))
        # parse connections
        node_connections = {}
        for connection in row:
            if "," not in connection:
                continue
            connection = connection.split(",")
            node_to = int(connection[0])
            distance = int(connection[1])
            node_connections[node_to] = distance
        graph[node] = node_connections
    file.close()
    return graph

file = "dijkstraData.txt"
graph = load_file(file)

def shortest_path(graph, source):
    visited_nodes = set()
    visited_nodes.add(source)
    total_nodes = len(graph.keys())

    # initially set shortest distances to infinity
    shortest_paths = graph.copy()
    for node in shortest_paths:
        shortest_paths[node] =  float("inf")
    shortest_paths[source] = 0

    while len(visited_nodes) != total_nodes:
        edges_out_of_visited = set()
        greedy_shortest_path = (None, float("inf"))
        for node in visited_nodes:
            for connected_to_node in graph[node]:
                if connected_to_node not in visited_nodes:
                    distance = shortest_paths[node] + graph[node][connected_to_node]
                    if distance < greedy_shortest_path[1]:
                        greedy_shortest_path = (connected_to_node, distance)
        visited_nodes.add(greedy_shortest_path[0])
        shortest_paths[greedy_shortest_path[0]] = greedy_shortest_path[1]
    return shortest_paths

source = 1
shortest_paths = shortest_path(graph, source)

# print in format requested by problem set
nodes = [7,37,59,82,99,115,133,165,188,197]
shortest_paths_for_nodes = []
for node in nodes:
    shortest_paths_for_nodes.append(shortest_paths[node])
print ",".join(map(lambda x: str(x),shortest_paths_for_nodes))
# 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
