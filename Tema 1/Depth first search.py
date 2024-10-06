# Depth.first search

def dfs(g):
    visited = set()
    n = len(g)
    for v in range(1,n):
        if v not in visited:
            dfsRec(v,visited, g)

def dfsRec(node,visited,g):
    print("Visiting node " + str(node))
    visited.add(node)
    for neigh in g[node]:
        if neigh not in visited:
            dfsRec(neigh,visited,g)

#Data definition

gAdjList = [
    [],
    [2,4,8],
    [1,3,4],
    [2,4,5],
    [1,2,3,7],
    [3,6],
    [5,7],
    [4,6,9],
    [1,9],
    [7,8]
]

visited = set()
dfsRec(1,visited,gAdjList)