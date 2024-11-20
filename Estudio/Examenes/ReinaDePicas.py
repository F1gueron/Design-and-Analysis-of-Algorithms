from collections import deque

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def notTurret(newX, newY,n,m,matriz):
    for cX, cY in moves:
        postX, postY = newX+cX, newY +cY
        if 0 <= postX < n and 0 <= postY < m:
            if matriz[postX][postY] == 't':
                return False
    return True


def bfs(matriz, n, m,start, recompensas, win):
    visited = set()
    x, y = start
    visited.add((x,y))
    q = deque()
    puntos = set()
    q.append((x,y,0,puntos, visited))
    while q:
        x,y,pasos,puntos, visited = q.popleft()
        if len(puntos) == recompensas and (x, y) == win:
            return pasos + 1
        for cX, cY in moves:
            newX, newY = x+cX, y +cY
            if 0 <= newX < n and 0 <= newY < m and matriz[newX][newY] != 'w' and notTurret(newX,newY,n,m,matriz) and (newX,newY) not in visited:
                nuevos_puntos = puntos.copy()
                nuevos_visited = visited.copy()
                if matriz[newX][newY] == 'r' and (newX, newY) not in nuevos_puntos:
                    nuevos_puntos.add((newX, newY))
                nuevos_visited.add((newX, newY))
                q.append((newX, newY, pasos + 1, nuevos_puntos, nuevos_visited))
    return -1


if __name__ == "__main__":
    n, m =  map(int, input().strip().split())
    matriz = []
    recompensas = 0
    for i in range(n):
        fila = list(map(str, input().strip().split()))
        matriz.append(fila)
        j = 0
        for c in fila:
            if c == 's':
                start = (i,j)
            if c == 'r':
                recompensas += 1
            if c == 'e':
                win = (i,j)
            j+=1
    print(bfs(matriz,n,m, start, recompensas, win))