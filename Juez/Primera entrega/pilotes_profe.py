from collections import deque


def bfsAux(g, visited, v):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True


def bfs(g):
    n = len(g)
    visited = [False] * n
    ncc = 0
    for v in range(0, n):
        if not visited[v]:
            bfsAux(g, visited, v)
            ncc += 1
    return ncc


if __name__ == '__main__':
    n,m = map(int, input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        a,b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    ncc = bfs(g)
    print(ncc)

