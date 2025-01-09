import copy
from math import inf

def inicializarLaberinto():
    F = 10
    C = 10
    fila = [0]*C
    laberinto = []
    for i in range(F):
        laberinto.append(fila[:])
    paredes = [[0, 2], [0, 7],[1, 0], [1, 2], [1, 5], [1, 6], [1, 8],[2,6],[2,8],[3,1],[3,4],[3,5],[3,6],[4,2],[4,3],[4,7],[5,5],[5,7],[6,0],[6,3],[6,4],[6,7],[6,9],[7,1],[7,2],[7,8],[7,9],[8,2],[8,4],[8,5]]
    for i in range(len(paredes)):
        laberinto[paredes[i][0]][paredes[i][1]] = inf
    return laberinto


def esFactible(laberinto,f,c):
    if f>=0 and f<len(laberinto) and c>=0 and c<len(laberinto[0]):
        return laberinto[f][c] == 0
    else:
        return False

def esSolucion(laberinto,f,c):
    return f == len(laberinto)-1 and c == len(laberinto)-1

def esMejor(sol1,sol2):
    return sol1[len(sol1)-1][len(sol1[0])-1] < sol2[len(sol2)-1][len(sol2[0])-1]

def salirDelLaberinto(laberinto,mejorSol,f,c,k):
    if esSolucion(laberinto,f,c):
        if esMejor(laberinto,mejorSol):
            mejorSol = copy.deepcopy(laberinto)
    else:
        desplazamientos=[[1,0],[0,1],[-1,0],[0,-1]]
        i = 0
        while not esSol and i < len(desplazamientos):
            if esFactible(laberinto,f+desplazamientos[i][0],c+desplazamientos[i][1]):
                laberinto[f+desplazamientos[i][0]][c+desplazamientos[i][1]] = k
                mejorSol = salirDelLaberinto(laberinto,mejorSol,f+desplazamientos[i][0],c+desplazamientos[i][1],k+1)
                laberinto[f + desplazamientos[i][0]][c + desplazamientos[i][1]] = 0
            i += 1
    return mejorSol

def imprimir(laberinto):
    for f in range(len(laberinto)):
        for c in range(len(laberinto[0])):
            if laberinto[f][c] == inf:
                print('*', end='\t')
            else:
                if laberinto[f][c] == 0:
                    print(' ', end='\t')
                else:
                    print(laberinto[f][c], end='\t')
        print()
    print()

def inicializarMejorSol(laberinto):
    mejorSol = copy.deepcopy(laberinto)
    mejorSol[len(laberinto)-1][len(laberinto[0])-1] = inf
    return mejorSol


# Prog Ppal:
laberinto = inicializarLaberinto()
mejorSol = inicializarMejorSol(laberinto)
f = 0
c = 0
k = 1
laberinto[f][c] = k
esSol = False
mejorSol = salirDelLaberinto(laberinto,mejorSol,f,c,k+1)
imprimir(mejorSol)