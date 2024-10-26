def greedy(actividades):
    actividades.sort(key=lambda x: x[2])
    sol = 0
    hora_terminada = 0
    for _,hora_inicio, hora_fin in actividades:
        if hora_inicio >= hora_terminada:
            sol += 1
            hora_terminada = hora_fin
    return sol




if __name__ == "__main__":
    N = int(input().strip())
    actividades = []
    for _ in range(N):
        datos = input().strip().split()
        nombre = datos[0]
        inicio = int(datos[1])
        fin = int(datos[2])
        actividades.append([nombre, inicio, fin])
    print(greedy(actividades))