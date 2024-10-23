
def getBestItem(candidates,data):
    bestRatio = -1
    bestItem = -1
    for c in candidates:
        ratio = data['profit'][c] / data['weight'][c]
        if ratio > bestRatio:
            bestRatio = ratio
            bestItem = c
    return bestItem

def isFeasible(data, bestItem, freeWeght):
    return (data['weight'][bestItem] <= freeWeght)

def greedyKnapsack(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    sol = [0] * n
    freeWeight = data['maxWeight']
    isSol = False
    while not isSol and candidates:
        bestItem = getBestItem(candidates, data)
        candidates.remove(bestItem)
        if isFeasible(data, bestItem, freeWeight):
            sol[bestItem] = 1.0
            freeWeight -= data['weight'][bestItem]
        else:
            sol[bestItem] = freeWeight/ data['weight'][bestItem]
            isSol = True
    return sol

#knapsack
#main program
data = {}
data['profit'] = [20, 30, 66, 40, 60]
data['weight'] = [10, 20, 30, 40, 50]
data['maxWeight'] = 100

sol  = greedyKnapsack(data)
print(sol)
