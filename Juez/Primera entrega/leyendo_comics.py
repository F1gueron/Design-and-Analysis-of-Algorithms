
import heapq

def topological_sort(comics, conexiones):
    g = []
    for _ in range(comics):
        g.append([])
    aristas = [0] * comics
    for a, b in conexiones:
        g[a].append(b)
        aristas[b] += 1
    q = []
    for node in range(comics):
        if aristas[node] == 0:
            heapq.heappush(q, node)
    topOrder = []
    while q:
        current = heapq.heappop(q)
        topOrder.append(current)
        for adj in g[current]:
            aristas[adj] -= 1
            if aristas[adj] == 0:
                heapq.heappush(q, adj)
    return topOrder

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    conexiones = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        conexiones.append((a, b))
    order = topological_sort(n, conexiones)
    print(" ".join(map(str, order)))