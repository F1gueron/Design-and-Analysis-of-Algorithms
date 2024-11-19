from collections import deque


def bfsAux(g,visited,i, fans):
    q = deque()
    visited[i] = True
    depth = 0
    q.append((i,depth))
    sol = []
    while q:
        aux, depth = q.popleft()
        sol.append(aux)
        for adjs in g[aux]:
            if not visited[adjs] and depth <= fans:
                q.append((adjs,depth+1))
                visited[adjs]=True
        return sol

def bfs(g, grade):
    n = len(g)
    visited = [False] * n
    fans = []
    for i in range(n):
        if not visited[i] and grade > 0:
            bfsAux(g, visited, i, grade)
        else:
            fans.append(0)
    return fans

if __name__ == "__main__":
    n = int(input())
    fans = []
    for i in range(n):
        fans.append([])
        grade,y,z = map(int, input().strip().split())
        g = []
        for _ in range(y):
            g.append([])
        for _ in range(z):
            a,b = map(int, input().strip().split())
            g[a].append(b)
            g[b].append(a)
        fans = bfs(g, grade)
    print(len(fans))