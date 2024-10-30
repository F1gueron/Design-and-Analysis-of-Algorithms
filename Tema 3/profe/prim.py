
from random import randint
def selectMin(candidates, visited):
    vertex= None
    weight= float('inf')
    for i in range(1,len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex=i
            weight=candidates[i]
    return vertex,weight

def prim(g):
    n=len(g)
    initial=randint(1,len(g)-1)
    visited=[False]*n
    sol=0
    visited[initial]=True
    candidates=[float('inf')]*n
    for (start, end, weight) in g[initial]:
        candidates[end]=weight
    for i in range(2,n):
        nextNode, cost = selectMin(candidates, visited)
        if cost<float('inf'):
            sol+=cost
            visited[nextNode]=True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end]= min(weight, candidates[end])
    return sol

g=[
[],
[(1,3,1),(1,4,2),(1,7,6)],
[(2,5,2),(2,6,4),(2,7,7)],
[(3,1,1),(3,4,2),(3,7,5)],
[(4,1,2),(4,3,3),(4,5,1),(4,6,9)],
[(5,2,2), (5,4,1), (5,7,8)],
[(6,2,4), (6,4,9)],
[(7,1,6), (7,2,7),(7,3,5), (7,5,8)]
]

sol=prim(g)
print(sol)