
movimientos = [(0,1),(1,0),(-1,0),(0,-1)]

def isFeasible(newPos, visited, matrix, N):
    newX, newY = newPos
    return 0 <= newX < N and 0 <= newY < N and (newX,newY) not in visited and matrix[newX][newY] != 3

def BT(N, cuadrado, Ex, Ey, pos, anillos, visitados, anillos_recogidos=0, index=0,mejorSol=float('inf')):
    Sx ,Sy = pos
    if pos == (Ex,Ey):
        if anillos == anillos_recogidos:
            if index < mejorSol:
                return index

    for dx,dy in movimientos:
        newPos = (dx + Sx, dy + Sy)
        if isFeasible(newPos, visitados, cuadrado, N):
            if cuadrado[dx + Sx][dy + Sy] == 1:
                anillos_recogidos +=1
            visitados.add(newPos)
            result = BT(N, cuadrado, Ex, Ey, newPos, anillos, visitados, anillos_recogidos, index + 1,mejorSol)
            if result is not None:
                mejorSol = min(mejorSol, result)
            visitados.remove(newPos)
            if cuadrado[dx + Sx][dy + Sy] == 1:
                anillos_recogidos -=1
    return mejorSol



if __name__ == "__main__":
    N = int(input().strip())
    cuadrado = []
    anillos = 0


    for _ in range(N):
        lista = list(map(int, input().strip().split()))
        anillos += lista.count(1)
        cuadrado.append(lista)
    Sx, Sy, Ex, Ey = map(int, input().strip().split())
    visitados = {(Sx, Sy)}
    resultado = BT(N, cuadrado, Ex, Ey, (Sx, Sy), anillos, visitados)

    print(resultado+1)