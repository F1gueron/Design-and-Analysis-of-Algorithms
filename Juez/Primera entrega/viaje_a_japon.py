from collections import deque


def bfs_aux(v, g, visited):
    visited[v] = True
    q = deque()
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


def bfs(g):
    n = len(g)
    visited = [False] * n
    disconnected_nodes = 0
    for v in range(n):
        if not visited[v]:
            bfs_aux(v, g, visited)
            disconnected_nodes += 1
    if disconnected_nodes == 1:
        print("PERFECTO")
    else:
        print("CAMBIA EL ITINERARIO")









if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    g = []
    for _ in range (n):
        g.append([])
    for _ in range(m):
        a,b = map(int,input().strip().split())
        g[a].append(b)

    if bfs(g):
        print("Si")

