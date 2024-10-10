from collections import deque


def bfs_aux(v, visited, fans,grade):
    q = deque()
    visited[v] = True
    q.append(v)
    fans.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                if aux == 0 and grade >= 3:
                    q.append(adj)
                fans.append(adj)





def bfs(g, grade):
    n = len(g)
    visited = [False] * n
    fans = []
    if grade > 0:
        bfs_aux(0,visited,fans,grade)
    else:
        fans.append(0)
    return len(fans)



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
        fans[i] = bfs(g, grade)
    for i in range(len(fans)):
        print(fans[i])