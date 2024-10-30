from math import ceil
from random import randint


def selectMin(candidates, visited):
    vertex= None
    weight= float('inf')
    for i in range(0,len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex=i
            weight=candidates[i]
    return vertex,weight


def prim(g):
    n = len(g)
    initial = randint(0,n)
    visited = [False] * n
    sol = 0
    visited [initial] = True
    candidates =[float('inf')] * n
    for (start, end, weight) in g[initial]:
        candidates[end]=weight
    for i in range(1,n):
        nextNode, cost = selectMin(candidates, visited)
        if cost<float('inf'):
            sol+=cost
            visited[nextNode]=True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end]= min(weight, candidates[end])
    return ceil(sol/5)

if __name__ == "__main__":
    N, M = map(int,input().strip().split())
    g = []
    for _ in range(N):
        g.append([])
    for _ in range(M):
        n1,n2,d = map(int,input().strip().split())
        g[n1].append([n1,n2,d])
        g[n2].append([n2,n1,d])
    sol = prim(g)
    print(sol)
