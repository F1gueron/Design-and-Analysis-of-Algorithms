
def dfsRec(node, graph, visit):
    visit.add(node)
    print("Visiting node " + str(node), end = "\t")
    for u in graph[node]:
        if u not in visit:
            dfsRec(u,graph,visit)


def dfs(g):
    n = len(g) - 1
    visited = set()
    for v in range(1, n + 1):
        if v not in visited:
            dfsRec(v,g,visited)


#Main prog.

#Adjacency List

graph_AdjList = [
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

dfs(graph_AdjList)

