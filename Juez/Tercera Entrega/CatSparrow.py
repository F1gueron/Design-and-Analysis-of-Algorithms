def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin, destiny):
    n = len(g)
    distances = [float('inf')] * (n)
    visited = [False] * (n)
    previous = [-1] * n


    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
        previous[end] = origin
    for _ in range(1, len(g)): #Bucle voraz
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if not visited[end] and distances[nextNode] + weight < distances[end]:
                distances[end] = min(distances[end], distances[start] + weight)
                previous[end] = nextNode

    path = []
    node = destiny
    while node != -1:
        path.append(node)
        node = previous[node]
    path.reverse()

    return distances[destiny], path


if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        c1, c2, d = map(int,input().strip().split())
        g[c1].append((c1,c2,d))
        g[c2].append((c2,c1,d))
    s,e = map(int,input().strip().split())

    sol,path = dijkstra(g,s,e)
    print(sol)
    for i in range(len(path)):
        print(path[i], end=" ")
