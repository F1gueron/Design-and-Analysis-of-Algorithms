from collections import deque


def bfsAux(g,visited,i):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        aux = q.popleft()
        for adjs in g[aux]:
            if not visited[adjs]:
                visited[adjs] = True
                q.append(adjs)


def bfs(g):
    n = len(g)
    visited =[False] *n
    sol = 0
    for i in range(n):
        if not visited[i]:
            bfsAux(g,visited,i)
            sol+=1
    return sol

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    num_connected_components = bfs(graph)
    print(num_connected_components)
