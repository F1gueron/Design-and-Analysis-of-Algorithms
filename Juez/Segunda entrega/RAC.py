


def greedy(actividades,hora_fin):
    disponible = [True] * hora_fin
    while feasible(disponible,)


if __name__ == "__main__":
    T = int(input().strip())
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
        greedy(actividades,hora_fin)