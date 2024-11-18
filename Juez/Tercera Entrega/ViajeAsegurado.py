

def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
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
    for _ in range(1, len(g)):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[nextNode] + weight)
    sol = -1
    for i in range(len(distances)):
        if distances[i] > sol:
            sol = distances[i]
    return sol





if __name__ == "__main__":
    n, m = map(int,input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        h1,h2,d = map(int, input().strip().split())
        g[h1].append((h1,h2,d))
        g[h2].append((h2, h1, d))
    max = -1
    for i in range(n):
        if dijkstra(g,i) > max:
            max = dijkstra(g,i)
    print(max)