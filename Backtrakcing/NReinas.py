def inicializarTablero(N):
    fila = [0] * N
    tablero = []
    for i in range(N):
        tablero.append(fila[:])
    return tablero

def imprimirSolucion(solucion):
    N = len(solucion)
    tablero = inicializarTablero(N)
    for fila in range(N):
        tablero[fila][solucion[fila]] = 1
        for columna in range(N):
            print(tablero[fila][columna],' ',end='')
        print()


def inicializarSolucion(N):
    return [-1] * N #la reina de la fila i está en la columna sol[i]

def esSolucion(sol, fila):
    return fila >= len(sol)

def esFactible(sol, fila, col):
    factible = True
    i = 1
    while factible and i <= fila:
        facibleCol = (sol[fila - i] != col)
        facibleDiag1 = (sol[fila - i] != col - i)
        facibleDiag2 = (sol[fila - i] != col + i)
        factible = facibleCol and facibleDiag1 and facibleDiag2
        i += 1
    return factible



def NReinasVA(sol, fila):
    if esSolucion(sol, fila):
        esSol = True
    else:
        esSol = False
        col = 0
        while not esSol and col < len(sol):
            if esFactible(sol, fila, col):
                sol[fila] = col
                (sol, esSol) = NReinasVA(sol, fila + 1)
                if not esSol:
                    sol[fila] = -1
            col += 1
    return sol, esSol



#NReinas
N = 4

sol = inicializarSolucion(N)
fila = 0
(sol, exito) = NReinasVA(sol,fila)

if exito:
    imprimirSolucion(sol)
else:
    print('La instancia del problema planteada no tiene solución')



