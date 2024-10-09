from collections import deque

def bfs(g, n, m, shift,win):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([(0, 0, shift)])
    visited = set()
    visited.add((0, 0))

    while q:
        x, y, shift = q.popleft()

        if (x,y) == win:
            return shift - 1

        for dx, dy in moves:
            newx, newy = x + dx, y + dy

            if 0 <= newx < n and 0 <= newy < m and (newx, newy) not in visited:
                if shift % 2 == 0:
                    if g[newx][newy] != -1:
                        visited.add((newx, newy))
                        q.append((newx, newy, shift + 1))
                else:
                    visited.add((newx, newy))
                    q.append((newx, newy, shift + 1))
    return -1

if __name__ == '__main__':
    n,m = map(int, input().strip().split())
    g = []
    win = None
    for i in range(n):
        row = list(map(int, input().split()))
        g.append(row)
    shift = 1
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                win = (i,j)
    distance = bfs(g,n,m,shift,win)
    if distance == -1:
        print("Case not found")
    else:
        print(distance)