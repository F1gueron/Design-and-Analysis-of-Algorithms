def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = -1
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
    for _ in range(len(g)):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances



if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    actividades = list(map(int, input().strip().split()))
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        c,d,l = map(int,input().strip().split())
        g[c].append((c,d,l))
        g[d].append((d,c,l))
    minDistTipo = [float('inf')] * len(set(actividades))
    for i in range(len(g)):
        distancias = dijkstra(g, i)
        for j in range(len(g)):
            if actividades[i] == actividades[j] and i != j:
                if distancias[j] < minDistTipo[actividades[j]]:
                    minDistTipo[actividades[j]] = distancias[j]
    for i in range(len(minDistTipo)):
        print(minDistTipo[i], end=" ")