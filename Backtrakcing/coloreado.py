#Algoritmo de vuelta atrás para el problema del coloreado de grafos

def inicializarGrafo():
    grafo = {}
    grafo['n'] = 4
    grafo['Adyacencia'] = [[1,2,3],[0],[0,3],[0,2]]
    return grafo

def inicializarSol(grafo):
    sol = [0] * grafo['n']
    return sol

def esSolucion(nodo, grafo):
    return nodo == grafo['n'] - 1

def esFactible(grafo, sol, nodo, color):
    factible = True
    AdyNodo = grafo['Adyacencia'][nodo]
    i = 0
    while factible and i < len(AdyNodo):
        if AdyNodo[i] < nodo:
            factible = (color != sol[AdyNodo[i]])
        i += 1
    return factible

def coloreadoVA(grafo, m, sol, numSols, nodo):
    if esSolucion(nodo, grafo): #caso base. Tengo una solución
        numSols += 1
        return numSols
    else: #caso recursivo. NO tengo una solución -> genero el siguiente nivel de hijos
        color = 1
        while color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                numSols = coloreadoVA(grafo, m, sol, numSols, nodo + 1)
                sol[nodo] = 0
            color += 1
    return numSols




#Defenición de datos
grafo = inicializarGrafo()
m = 3 #número de colores
sol = inicializarSol(grafo)
numSols = 0
nodo = 0
numSols = coloreadoVA(grafo, m, sol, numSols, nodo)
print(numSols)




