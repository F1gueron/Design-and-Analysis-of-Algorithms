import heapq


def topSort(n,conexiones):
    g = []
    aristas = []
    visited = [False]* n
    for _ in range(n):
        g.append([])
    for con in conexiones:
        a,b = con
        g[a].append(b)
        aristas[a] += 1
    q = []
    sol =[]
    for i in range(len(aristas)):
        if aristas[i] == 0:
            heapq.heappush(q, i)
            visited[i]= True
    while q:
        aux = heapq.heappop()
        sol.append(aux)
        for adjs in g[aux]:
            if not visited[adjs]:
                aristas[adjs] -= 1
                if aristas[adjs] == 0:
                    heapq.heappush(q,adjs)
                    visited[adjs] = True
        return sol




if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    conexiones = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        conexiones.append((a, b))
    order = topSort(n, conexiones)
    print(" ".join(map(str, order)))