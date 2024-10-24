
def best(actividades, candidatos):
    bestTime = float('inf')
    bestItem = -1
    for i in candidatos:
        if actividades[i][1] - actividades[i][0] < bestTime:
            bestTime = actividades[i][1] - actividades[i][0]
            bestItem = i

    return bestItem, bestTime


def isSol(disponible, mejor_tiempo):
    tiempo_libre = 0
    for i in range(len(disponible)):
        if disponible[i]:
            tiempo_libre += 1
            if tiempo_libre >= mejor_tiempo:
                return True
        else:
            tiempo_libre = 0
    return False


def isFeasible(disponible, actividad):
    for i in range(actividad[0]-1,actividad[1]):
        if not disponible[i]:
            return False
    return True


def greedy(actividades,hora_fin):
    disponible = [True] * hora_fin
    candidatos = set()
    for i in range(len(actividades)):
        candidatos.add(i)
    sol = 0
    mejor_actividad, mejor_tiempo = best(actividades, candidatos)
    while candidatos and isSol(disponible, mejor_tiempo):
        if isFeasible(disponible,actividades[mejor_actividad]):
            for i in range(actividades[mejor_actividad][0], actividades[mejor_actividad][1]):
                disponible[i - 1] = False
            sol += 1
        candidatos.remove(mejor_actividad)
        mejor_actividad, mejor_tiempo = best(actividades, candidatos)
    return sol




if __name__ == "__main__":
    T = int(input().strip())
    sol = []
    for i in range(T):
        N = int(input().strip())
        lista_horas = list(map(int, input().strip().split()))
        hora_inicio = min(lista_horas)
        hora_fin = max(lista_horas)
        actividades=[]
        for i in range(N):
            inicio = lista_horas[2 * i]
            fin = lista_horas[2 * i +1]
            actividades.append([inicio,fin])
        sol.append(greedy(actividades,hora_fin))
    for result in sol:
        print(result)
