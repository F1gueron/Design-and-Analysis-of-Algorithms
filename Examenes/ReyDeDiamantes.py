def selectMinDistance(visited, distances):
    bestDistance = float('inf')
    bestItem = -1
    for i in range(len(distances)):
        if not visited[i] and distances[i] < bestDistance:
            bestDistance = distances[i]
            bestItem = i
    return bestItem

def dijsktra(g, juegos, start, end, sequence):
    n = len(g)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0
    visited[start] = True
    sol = []

    expected = []
    for c in sequence:
        expected.append(c)
    for start, end, weight in g[start]:
        distances[end] = weight
    if expected[0] == juegos[start][1]:
        sol.append(juegos[start][0])
        expected.remove(expected[0])
    for i in range(n):
        nextNode = selectMinDistance(visited,distances)
        visited[nextNode] = True
        if expected[0] == juegos[nextNode][1]:
            sol.append(juegos[nextNode][0])
            expected.remove(expected[0])
            if len(expected) == 0:
                return sol
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)
    if expected:
        return -1
    else:
        return sol


if __name__ == "__main__":
    n,m,c = map(int,input().strip().split())
    sol = []
    for _ in range(c):
        g = []
        juegos = []
        for _ in range(n):
            g.append([])
        for _ in range(m):
            a,b,d = map(int,input().strip().split())
            g[a].append((a,b,d))
            g[b].append((b,a,d))
        tipos = set()
        for _ in range(n):
            e,f = input().strip().split()
            e = int(e)
            tipos.add(f)
            juegos.append((e,f))
        start, end, sequence = input().strip().split()
        start = int(start)
        end = int (end)
        print(*dijsktra(g,juegos, start, end, sequence))
