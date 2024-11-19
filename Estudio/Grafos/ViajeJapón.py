from collections import deque


def dfsAux(g, visited, i):
    q = deque()
    visited[i] = True
    q.append(i)
    while q:
        aux = q.popleft()
        for adjs in g[aux]:
            if not visited[adjs]:
                q.append(adjs)
                visited[adjs] = True


def dfs(g, param, n):
    visited = [False] * n
    visited[param] = True
    components = 0
    for i in range(n):
        if not visited[i]:
            dfsAux(g,visited,i)
            components += 1
    return components == 1


def invert_graph(g, n):
    auxG = []
    for i in range(n):
        auxG.append([])

    for i in range(n):
            for a in g[i]:
                auxG[a].append(i)
    return auxG


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)

    exist_path = False
    if dfs(g, 0, n):
        inverted_g = invert_graph(g, n)
        if dfs(inverted_g, 0, n):
            exist_path = True

    if exist_path:
        print("PERFECTO")
    else:
        print("CAMBIA EL ITINERARIO")