
def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates

def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    candidates = sortCandidates(g)
    components = list(range(len(g))) #crea un array [0,1,2, ..., 7]
    count = len(components)
    sol = 0
    #bucle voraz
    i = 0
    while count > 1 and len(candidates) > i: #isSol
        (weight, start, end) = candidates[i] #getBestItem
        if components[start] != components[end]:
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return sol

#Kruskal
g = [
    [(0, 2, 1), (0, 3, 2), (0, 6, 6)],  # adyacentes del nodo 0
    [(1, 4, 2), (1, 5, 4), (1, 6, 7)],
    [(2, 0, 1), (2, 3, 3), (2, 6, 5)],
    [(3, 0, 2), (3, 2, 3), (3, 4, 1), (3, 5, 9)],
    [(4, 1, 2), (4, 3, 1), (4, 6, 8)],
    [(5, 1, 4), (5, 3, 9)],
    [(6, 0, 6), (6, 1, 7), (6, 2, 5), (6, 4, 8)]
]


sol = kruskal(g)
print(sol)