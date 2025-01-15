
def selectBestItem(concursantes, cualidad, t,candidates):
    bestItem = -1
    bestRatio = -1
    for i in candidates:
        if concursantes[cualidad]/t > bestRatio:
            bestRatio = concursantes[cualidad]/t
            bestItem = i
    return bestItem

def qsell(cualidad, m, t, concursantes):
    n = len(concursantes)
    candidates = []
    for i in range(n):
        candidates.add(i)
    timeleft = t
    sol = 0
    while candidates and timeleft > 0:
        next = selectBestItem(concursantes, cualidad, t, candidates)
        candidates.remove(next)
        if timeleft >= concursantes[4]:
            timeleft -= concursantes[4]
            sol += concursantes[cualidad]
        else:
            ratio = timeleft/concursantes[4]
            timeleft = 0
            sol += ratio*concursantes[cualidad]
        solNames.append(concursantes[0])


if __name__ == "__main__":
    n = int(input())
    cualidad = input()
    concursantes = []
    for _ in range(n):
        m, t = map(int,input().strip().split())
    for _ in range(n):
        datos = input()
        nombre = datos[0]
        b = int(datos[1])
        i = int(datos[2])
        k = int(datos[3])
        t = int(datos[4])
        concursantes.append((nombre, b, i, k, t))
    if cualidad is "kindess":
        cualidad = 3
    elif cualidad is "intelligence":
        cualidad = 2
    elif cualidad is "beauty":
        cualidad = 1
    qsell(cualidad, m, t, concursantes)