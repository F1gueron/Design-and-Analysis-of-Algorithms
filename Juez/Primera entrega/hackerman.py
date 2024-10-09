from collections import deque


def bfsAux(v, g, visited):
    q = deque()
    path = deque()
    visited[v] = True
    q.append(v)
    path.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True
                path.append(adj)
    connected_computers = len(path)
    cost = 0
    if connected_computers >= 2:
        path.popleft()
        path.pop()
        while path:
            cost += reinforcement_cost[path.pop()]
    return cost



def bfs(g):
    n = len(g)
    visited = [False] * n
    cost = 0
    for v in range(n):
        if not visited[v]:
            cost += bfsAux(v,g,visited)
    return cost






if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    reinforcement_cost = []
    g = []
    for _ in range(n):
        reinforcement_cost.append(int(input().strip()))
        g.append([])
    for _ in range(m):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)
    # For printing g
    #for fila in g:
    #    print(' '.join(map(str, fila)))
    cost = bfs(g)
    print(cost)