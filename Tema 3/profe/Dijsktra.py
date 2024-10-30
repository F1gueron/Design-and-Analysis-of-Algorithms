def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin):
    n = len(g) - 1
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
    for _ in range(2, len(g)): #Bucle voraz
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances

#Dijkstra
g = [
    [],
    [(1,2,5),(1,4,3)],
    [(2,5,1)],
    [],
    [(4,2,1),(4,3,11),(4,5,6)],
    [(5,3,1)]
]

node = 1
sol = dijkstra(g, node)

print(sol)
