import random

# load file
file = open("kargerMinCut.txt")
nodes = {};
for line in file :
  row = line.split("\t")
  nodes[row[0]] = row[1:-1] # last element is line break
file.close()

# 1 random contraction
def random_contraction(graph_to_copy):
    # makes copy to prevent mutation
    graph = graph_to_copy.copy()
    while len(graph) > 2:
        # randomly choose 2 nodes that are connected (i.e. an edge)
        nodeA = random.choice(graph.keys())
        nodeB = random.choice(graph[nodeA])
        # store merged connections in nodeAB (to prevent mutation)
        # we use nodeA's id
        nodeAB = []
        for i in graph[nodeA]:
            # delete self loops
            if i != nodeA and i != nodeB:
                nodeAB.append(i)
        for j in graph[nodeB]:
            # change references to nodeB to nodeA; makes copy to prevent mutation
            graph[j] = graph[j][:]
            graph[j].remove(nodeB)
            graph[j].append(nodeA)
            # delete self loops
            if j != nodeA and j != nodeB:
                nodeAB.append(j)
        # merge
        graph.pop(nodeB)
        graph[nodeA] = nodeAB
    return len(graph[graph.keys()[0]])

def repeat_random_contractions(graph):
    min_cut = -1
    n = len(graph)
    for i in range(n):
        cut = random_contraction(graph)
        if cut < min_cut or min_cut == -1:
            min_cut = cut
    return min_cut

print repeat_random_contractions(nodes)
