movimientos = [(0,1),(1,0),(-1,0),(0,-1)]


def isFeasible(newPos, visited, matrix, N, M):
    newX, newY = newPos
    return 0 <= newX < N and 0 <= newY < M and (newX,newY) not in visited and matrix[newX][newY] != -1


def BT(N, M, matrix, E, X, Y, D,visited, pos, index = 0,enemigos=0):
    actX, actY = pos
    if index == D:
        return enemigos==E
    for dx,dy in movimientos:
        newPos = (dx+actX,dy+actY)
        if isFeasible(newPos,visited,matrix,N,M):
            visited.add(newPos)
            if matrix[dx+actX][dy+actY] == 1:
                enemigos +=1
            if BT(N, M, matrix, E, X, Y, D, visited, newPos, index+1, enemigos):
                return True
            if matrix[dx+actX][dy+actY] == 1:
                enemigos -=1
            visited.remove(newPos)






if __name__ == "__main__":
    N,M,E = map(int, input().strip().split())
    matrix = []
    for _ in range(N):
        lista = list(map(int,input().strip().split()))
        matrix.append(lista)
    X,Y,D = map(int, input().strip().split())
    visited = set()
    visited.add((X,Y))
    if BT(N,M,matrix,E,X,Y,D, visited,(X,Y)):
        print("ATACA")
    else:
        print("CORRE")