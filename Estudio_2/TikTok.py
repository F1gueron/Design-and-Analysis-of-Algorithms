from collections import deque


def bfs_aux(i, g, visited, m, amigos,depth = 1):
    q = deque()
    visited[i] = True
    q.append(i)
    amigos = 1
    while q:
        aux = q.popleft()
        if depth < m:
            for adj in g[aux]:
                if adj not in visited:
                    q.append(adj)
                    visited[adj] = True
                    amigos += 1
    return amigos


def bfs(g, m):
    n = len(g)
    amigos = 0
    visited = [False] * n
    for i in range(n):
        if i not in visited:
            bfs_aux(i,g,visited,m, amigos)
    return amigos


if __name__ == "__main__":
    n = int(input())
    m,k,c = map(int,input().strip().split())
    g = [[]for i in range(k)]
    for _ in range(c):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)
    print(bfs(g,m))