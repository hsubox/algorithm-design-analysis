# in this problem set, instead of using stacks with pop(0) and insert(0, x)
# the reverse is done, i.e. pop(len()-1) and append
# this allows the algorithm to run significantly faster

# load file
file = open("SCC.txt")
# file = open("SCC_test.txt")
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
    graph_fwd[head].append(tail)
    # add to reverse graph
    if tail not in graph_rev:
      graph_rev[tail] = []
    graph_rev[tail].append(head)
file.close()

visited = set()
f = [] # stores finishing times of each node
f_set = set() # this is a copy of f as a set for fast searching
def visit(graph, x):
    stack = [];
    stack.append(x)
    while len(stack) > 0:
        i = stack.pop(len(stack)-1)
        if i not in visited:
            visited.add(i)
            stack.append(i)
            if i in graph: # may not exist in graph if it doesn't point anywhere
                for j in graph[i]:
                    if j not in visited:
                        stack.append(j)
        else:
            if i not in f_set:
                f.append(i)
                f_set.add(i)

def visit_loop(graph):
    for i in graph:
        visit(graph, i)
    f.reverse()

assigned = set()
l = {} # stores leaders of each node

def assign(graph, x, leader):
    stack = [];
    stack.append(x)
    while len(stack) > 0:
        i = stack.pop(len(stack)-1)
        if i not in assigned:
            assigned.add(i)
            if i in graph: # may not exist in graph if it doesn't point anywhere
                for j in graph[i]:
                    if j not in assigned:
                        stack.append(j)
            # add this to the leader's group
            if leader not in l:
                l[leader] = []
            l[leader].append(i)

def assign_loop(graph):
    for i in f:
        assign(graph, i, i)

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
# print in format requested by problem set
top = top_sccs(leaders, 5)
print ",".join(map(lambda x: str(x),top))
