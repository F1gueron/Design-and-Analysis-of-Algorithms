from collections import deque


def dfsAux(start, g, visited,depth):
    q = deque()
    visited[start] = True
    q.append((start,0))
    while q:
        aux, depth = q.popleft()
        visited[aux] = True
        if depth == 1:
            q = deque()
        for adj in g[aux]:
            if not visited[adj]:
                q.append((adj,depth+1))

def dfs(g, start):
    n = len(g)
    visited = [False] * n
    depth = 0
    dfsAux(start, g, visited,depth)

    return all(visited)


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    reinforcement_cost = []
    g = []

    for _ in range(n):
        reinforcement_cost.append(int(input().strip()))
        g.append([])

    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    cost = 0
    for i in range(n):
        if not dfs(g, i):
            cost += reinforcement_cost[i]
    print(cost)
