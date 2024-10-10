def isSol(cost):
    return cost == 0


def isFeasible(coin, cost):
    return coin <= cost


def greedyCoins(cost, cand, sol):
    current_coin = 0
    while not isSol(cost):
        if not isFeasible(cand[current_coin],cost):
            current_coin += 1
        else:
            sol[current_coin] += 1
            cost -= cand[current_coin]
    return sol


def printSol(sol, cand):
    for i in range(len(cand)):
        if sol[i] != 0:
            print(f"{sol[i]} monedas de {cand[i]}")
            print(sol[i],"billetes dea", cand[i])




cost = 437
cand = [500, 200, 100, 50, 10, 5, 2, 1]


sol = [0] * len(cand)

sol = greedyCoins(cost, cand, sol)
printSol(sol, cand)
