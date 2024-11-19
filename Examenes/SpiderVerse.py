def selectMinDis(visitados, distances):
    index = -1
    minDist=float('inf')
    for i in range(len(distances)):
        if not visitados[i] and distances[i] < minDist:
            index = i
            minDist = distances[i]

    return index

def djikstra(g, origin):
    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[origin] =0
    previous = [-1] * n

    for _ in range(n):
        nextNode = selectMinDis(visited,distances)
        visited[nextNode] = True
        for start,end,weight in g[nextNode]:
            if distances[end] > distances[start] + weight:
                previous[end] = start
                distances[end] = distances[start]+weight

    maxDistance = max(distances)
    for i in range(len(distances)):
        if maxDistance == distances[i]:
            index = i
    path = []
    act = index
    while previous[act] != -1:
        path.append(act)
        act = previous[act]
    path.append(origin)
    path.reverse()
    return maxDistance,path,index

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        a,b,c = map(int,input().strip().split())
        g[a].append((a, b, c))
        g[b].append((b, a, c))
    origin = int(input().strip())
    max_distance,path,index=djikstra(g, origin)
    print(f"{index ," " , max_distance}")
    print(*path)