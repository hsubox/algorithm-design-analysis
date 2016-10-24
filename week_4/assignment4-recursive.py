# works on small data sets, runs out of resources for large ones such as that in the problem set

# load file
# file = open("SCC.txt")
file = open("SCC_test.txt")
graph_fwd = {};
graph_rev = {};
lines = file.read().split('\n')
for line in lines[:-1]: # file ends with extra line break
    row = line.split(" ")
    head = int(row[0])
    tail = int(row[1])
    # add to forward graph
    if head not in graph_fwd:
      graph_fwd[head] = []
    graph_fwd[head] += [tail]
    # add to reverse graph
    if tail not in graph_rev:
      graph_rev[tail] = []
    graph_rev[tail] += [head]
file.close()

visited = set()
f = [] # stores finishing times of each node

def visit(graph, i):
    if i not in visited:
        visited.add(i)
        if i in graph:
            for j in graph[i]:
                visit(graph, j)
        f.insert(0, i)

def visit_loop(graph):
    for i in graph:
        visit(graph, i)

assigned = set()
l = {} # stores leaders of each node

def assign(graph, i, leader):
    if i not in assigned:
        assigned.add(i)
        if i in graph:
            for j in graph[i]:
                assign(graph, j, leader)

        # if this leader doesn't exist, initialize
        if leader not in l:
            l[leader] = []
        # add this to the leader's group
        l[leader] += [i]

def assign_loop(graph):
    for i in f:
        assign(graph, i, i) # 3rd argument is leader

def kosarajus(graph_fwd, graph_rev):
    visit_loop(graph_rev)
    print f
    assign_loop(graph_fwd)
    print l
    return l

def top_sccs(l, n):
    size = []
    for i in l:
        size.append(len(l[i]))
    size.sort(reverse=True)
    # if n > # of sccs, then the rest will be 0
    size.extend([0]*n)
    return size[:n]

leaders = kosarajus(graph_fwd, graph_rev)
print top_sccs(leaders, 5)
