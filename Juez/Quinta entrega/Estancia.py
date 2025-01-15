def backtrack(objetos, peso_max, beneficio_min, index=0, actual=None, mejor_sol=None):
    if actual is None:
        actual = {"objetos": [], "peso": 0, "beneficio": 0}
    if mejor_sol is None:
        mejor_sol = {"objetos": [], "peso": 0, "beneficio": 0}
    if index == len(objetos):
        print("Entra")
        if actual["peso"] <= peso_max:
            if actual["beneficio"] > mejor_sol["beneficio"]:
                mejor_sol["objetos"] = list(actual["objetos"])
                mejor_sol["beneficio"] = actual["beneficio"]
                mejor_sol["peso"] = actual["peso"]
        return mejor_sol
    mejor_sol = backtrack(objetos, peso_max, beneficio_min, index + 1, actual, mejor_sol)
    obj_nombre, obj_peso, obj_beneficio = objetos[index]
    if actual["peso"] + obj_peso <= peso_max:
        actual["objetos"].append(obj_nombre)
        actual["peso"] += obj_peso
        actual["beneficio"] += obj_beneficio

        mejor_sol = backtrack(objetos, peso_max, beneficio_min, index + 1, actual, mejor_sol)

        actual["objetos"].pop()
        actual["peso"] -= obj_peso
        actual["beneficio"] -= obj_beneficio

    return mejor_sol


if __name__ == "__main__":
    N, P, B = map(int, input().strip().split())
    objetos = []

    for _ in range(N):
        datos = input().strip().split()
        nombre = datos[0]
        peso = int(datos[1])
        beneficio = int(datos[2])
        objetos.append((nombre, peso, beneficio))


    winCon = backtrack(objetos, P, B)
    winCon["objetos"].sort()
    for obj in winCon["objetos"]:
        print(obj, end=" ")
    print()
    sum1 = winCon["peso"]
    sum2 = winCon["beneficio"]
    print(f"{sum1} {sum2}")

    if winCon["beneficio"] > B:
        print("SE VA")
    else:
        print("VUELVE")

