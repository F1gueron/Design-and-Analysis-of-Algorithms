#Sea W un conjunto de enteros no negativos y M un entero positvo. Se pide diseñar e implementar un algoritmo para
# encontrar todos los subconjuntos de de W cuya suma sea exactamente M
# Prog Ppal:

def esSolucion(W, M, sol, k):
    suma = 0
    for i in range(k + 1):
        if sol[i] == 1:
            suma += W[i]
    return suma == M

def esFactible(W, M, sol, k):
    suma = 0
    for i in range(k + 1):
        suma += W[i] * sol[i]

    return suma <= M

def VueltaAtrasSubconjuntos(W, M, sol, k):
    if esSolucion(W, M, sol, k): #es un solucion
        print(sol)
    else: #no tengo una solución
        if k < len(sol) - 1:
            k += 1
            VueltaAtrasSubconjuntos(W, M, sol, k)
            if esFactible(W, M, sol, k):
                sol[k] = 1
                VueltaAtrasSubconjuntos(W, M, sol, k)
                sol[k] = 0

W = [7,2,3,4,9]
#sol = [1, 0, ¿1?
M = 9

#sol 1 = [1,1,0,0,0]
#sol 2 = [0,0,0,0,1]


sol = [0] * len(W)
k = -1
VueltaAtrasSubconjuntos(W, M, sol, k)

