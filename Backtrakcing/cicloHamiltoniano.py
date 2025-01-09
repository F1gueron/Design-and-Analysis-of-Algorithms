#Algoritmo de vuelta atrás para detectar el número de ciclos hamilitonianos

def test_graph():

    """
    (0)---(1)---(2)
      \  /  \  /
      (3)---(4)
    """

    edges = [(0,1), (0,3), (1,2), (1,3), (1,4), (2,4), (3,4)]
    v = 5

    graph = [[] for _ in range(v)]
    for (start, end) in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def esSolucion(graph, sol, nodo):
    return nodo == sol[0] and len(sol) == len(graph) + 1

def esFactible(nodo, sol, n):
    return nodo not in sol or (nodo == sol[0] and len(sol) == n)

def hamiltonianVA(graph, nodo, sol, numSols):
    if esSolucion(graph, sol, nodo):
        numSols += 1
    else:
        for ady in graph[nodo]:
            if esFactible(ady, sol, len(graph)):
                sol.append(nodo)
                numSols = hamiltonianVA(graph, ady,sol, numSols)
                sol.pop()
    return numSols

graph = test_graph()
ini = 0
sol = [ini]
numSols = 0
numSols = hamiltonianVA(graph, ini, sol, numSols)

print(numSols)
