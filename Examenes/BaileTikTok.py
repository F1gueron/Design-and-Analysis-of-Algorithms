from collections import deque


def bfsAux(g, visited,m):
    q = deque()
    depth = 1
    q.append((0,depth))
    visited[0] = True
    sol = 1
    while q:
        aux, depth = q.popleft()
        if depth < m:
            for adjs in g[aux]:
                if not visited[adjs]:
                    q.append((adjs,depth+1))
                    visited[adjs] = True
                    sol+=1
    return sol


def bfs(g, m):
    n = len(g)
    visited = [False] * n
    sol = 0
    sol = bfsAux(g,visited,m)
    return sol


if __name__ == "__main__":
    n = int(input().strip())
    sol = []
    for _ in range(n):
        m,k,c = map(int,input().strip().split())
        g = []
        for _ in range(k):
            g.append([])
        for _ in range(c):
            a,b = map(int,input().strip().split())
            g[a].append(b)
            g[b].append(a)
        sol.append(bfs(g,m))
    print(*sol)