#11.- Dado un conjunto de n enteros, necesitamos decidir si puede ser descompuesto en dos
#subconjuntos disjuntos cuyos elementos sumen la misma cantidad.
#PROGRAMA PRINCIPAL

def imprimirSol(tupla,conjunto):
    print('Conjunto -1: ',end='')
    for i in range(len(tupla)):
        if tupla[i] == -1:
            print(conjunto[i],end=' ')
    print()
    print('Conjunto 1: ', end='')
    for i in range(len(tupla)):
        if tupla[i] == 1:
            print(conjunto[i], end=' ')
    print()

def esSolucion(conj, k, sol):
    if k < len(sol):
        return False
    else:
        suma = 0
        for i in range(len(sol)):
            suma += sol[i] * conj[i]
    return suma == 0

def esFactible(k, sol):
    return k < len(sol)

def sumaVA(conj, k, sol):
    if esSolucion(conj, k, sol): #tengo una solución
        esSol = True
    else:
        conjuntosPosibles = [-1, 1]
        esSol = False
        if esFactible(k, sol):
            i = 0
            while i < len(conjuntosPosibles) and not esSol:
                sol[k] = conjuntosPosibles[i]
                esSol, sol = sumaVA(conj, k + 1, sol)
                if not esSol:
                    sol[k] = 0
                i += 1

    return esSol,sol


#no tengo una solución


conjunto = [3, 8, 7, 2, 4]

sol = [0] * len(conjunto)
k = 0
(esSol, sol) = sumaVA(conjunto, k, sol)

if esSol:
    print('Se ha encontrado una solución y es:')
    print(sol)
    #imprimirSol(sol)
else:
    print('No se ha encontrado una solución')