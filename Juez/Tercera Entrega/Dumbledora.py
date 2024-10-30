from math import ceil
from random import randint

def selectMin(candidates, visited):
    vertex= None
    weight= float('inf')
    actual = None
    for i in range(0,len(candidates)):
        if not visited[i] and candidates[i][0] < weight:
            vertex=i
            weight=candidates[i][0]
            actual = candidates[i][1]
    return vertex,weight, actual


def prim(g):
    n = len(g)
    initial = 0
    visited = [False] * n
    sol = 0
    visited [initial] = True
    candidates =[(float('inf'), None)] * n
    instalacion = [0] * n
    for (start, end, weight) in g[initial]:
        candidates[end]=(weight, start)
    for i in range(1,n):
        nextNode, cost, actual = selectMin(candidates, visited)
        if cost<float('inf'):
            instalacion[nextNode] += cost
            instalacion[actual] += cost
            sol+=cost
            visited[nextNode]=True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end]= [min(weight, candidates[end][0]), nextNode]
    return sol, instalacion

if __name__ == "__main__":
    N, M = map(int,input().strip().split())
    g = []
    for _ in range(N):
        g.append([])
    for _ in range(M):
        n1,n2,d = map(int,input().strip().split())
        g[n1].append([n1,n2,d])
        g[n2].append([n2,n1,d])
    sol, instalacion = prim(g)
    print("Coste total: ",sol)
    for i in range(len(instalacion)):
        print(f"H{i}: {instalacion[i]}")
