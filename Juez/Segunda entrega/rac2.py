

def greedy(actividades):
    actividades.sort(key=lambda x: x[1])
    sol = 0
    hora_terminada = 0
    for hora_inicio, hora_fin in actividades:
        if hora_inicio >= hora_terminada:
            sol += 1
            hora_terminada = hora_fin
    return sol




if __name__ == "__main__":
    T = int(input().strip())
    sol = []

    for _ in range(T):
        N = int(input().strip())
        lista_horas = list(map(int, input().strip().split()))
        actividades = []
        for i in range(N):
            inicio = lista_horas[2 * i]
            fin = lista_horas[2 * i +1]
            actividades.append([inicio, fin])
        sol.append(greedy(actividades))
    for result in sol:
        print(result)
