def dfsRec(node, graph, visit):
    visit.add(node)
    for u in graph[node]:
        if u not in visit:
            dfsRec(u, graph, visit)

def dfs(g, starting_node, total_nodes):
    visited = set()
    dfsRec(starting_node, g, visited)

    return len(visited) == total_nodes

def invert_graph(g):
    n = len(g)
    inverted = []
    for _ in range(n):
        inverted.append([])
    for node in range(len(g)):
        for v in g[node]:
            inverted[v].append(node)
    return inverted

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)

    exist_path = False
    if dfs(g, 0, n):
        inverted_g = invert_graph(g)
        if dfs(inverted_g, 0, n):
            exist_path = True

    if exist_path:
        print("PERFECTO")
    else:
        print("CAMBIA EL ITINERARIO")
