
def selectBestItem(distances,visited):
    minDist = float('inf')
    bestItem = -1
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem



def dijkstra(g):
    n = len(g)
    visited = [False] *n
    distances = [float('inf')]*n
    distances[0] = 0

    for start,end,weight in g[0]:
        distances[end] = weight
    for _ in range(1,n):
        nextNode = selectBestItem(distances,visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start]+weight)
    time =0
    for i in range(len(distances)):
        time += distances[i]
    return time



if __name__ == "__main__":
    n,m,t = map(int,input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        h_1,h_2,d = map(int,input().strip().split())
        g[h_1].append((h_1,h_2,d))
        g[h_2].append((h_2, h_1, d))
    sol = dijkstra(g)

    if sol <= t:
        print(sol)
    else:
        print("Aleg, ¡a decorar!")