from collections import deque


moves = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(g,n,m, win):
    visited = set()
    visited.add((0,0))
    q = deque()
    shift = 1
    x = 0
    y = 0
    q.append((x,y, shift))
    while q:
        x,y,shift = q.popleft()
        for directions in moves:
            posX, posY = x+directions[0], y+directions[1]
            if (posX,posY) == win:
                return shift
            if 0 <= posX <= n and 0 <= posY <= m and (posX,posY) not in visited:
                if shift % 2 == 0 and g[posX][posY] != 1:
                    visited.add((posX,posY))
                    q.append((posX,posY,shift+1))
                else:
                    visited.add((posX,posY))
                    q.append((posX, posY, shift + 1))
    return -1





if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = []
    win = None
    for i in range(n):
        row = list(map(int, input().split()))
        g.append(row)
    shift = 1
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                win = (i, j)
    distance = bfs(g, n, m, win)
    if distance == -1:
        print("Case not found")
    else:
        print(distance)
