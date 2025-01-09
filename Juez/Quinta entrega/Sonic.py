def BT(N, cuadrado, Sx, Sy, Ex, Ey, pos, anillos, visitados, anillos_recogidos, sol=0, mejorSol=float('inf')):
    if pos == (Ex, Ey) and anillos == 0:
        return min(sol, mejorSol)

    if sol >= mejorSol:
        return mejorSol

    actX, actY = pos
    movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for moveX, moveY in movimientos:
        nuevaX = actX + moveX
        nuevaY = actY + moveY
        nueva_pos = (nuevaX, nuevaY)

        if (0 <= nuevaX < N and 0 <= nuevaY < N and
                cuadrado[nuevaX][nuevaY] != 3 and
                nueva_pos not in visitados):

            nuevo_visitados = visitados | {nueva_pos}
            nuevo_anillos_recogidos = anillos_recogidos.copy()

            if cuadrado[nuevaX][nuevaY] == 1 and nueva_pos not in anillos_recogidos:
                nuevo_anillos_recogidos.add(nueva_pos)
                temp = BT(N, cuadrado, Sx, Sy, Ex, Ey, nueva_pos, anillos - 1,
                          nuevo_visitados, nuevo_anillos_recogidos, sol + 1, mejorSol)
                mejorSol = min(mejorSol, temp)
            else:
                temp = BT(N, cuadrado, Sx, Sy, Ex, Ey, nueva_pos, anillos,
                          nuevo_visitados, nuevo_anillos_recogidos, sol + 1, mejorSol)
                mejorSol = min(mejorSol, temp)

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
    anillos_recogidos = set()
    resultado = BT(N, cuadrado, Sx, Sy, Ex, Ey, (Sx, Sy), anillos, visitados, anillos_recogidos)

    print(resultado+1)