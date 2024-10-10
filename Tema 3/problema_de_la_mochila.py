def gest_best_item(candidates, data):
    best_ratio = -1
    best_item = -1
    for c in candidates:
        ratio = data['profit'][c] / data['weight'][c]
        if ratio > best_ratio:
            best_ratio = ratio
            best_item = c
    return best_item




def is_feasible(data, best_item, free_weight):
    return data['weight'][best_item] <= free_weight


def greedy_knapsack(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    sol =[0] * n
    free_weight = data['max_weight']
    is_sol = False
    while not is_sol and candidates:
        best_item = gest_best_item(candidates, data)
        candidates.remove(best_item)
        if is_feasible(data,best_item,free_weight):
            sol[best_item] = 1.0
            free_weight -= data['weight'][best_item]
        else:
            sol[best_item] = free_weight / data['weight'][best_item]
            is_sol = True
    return sol

def calculate_cost(sol, data):
    profit = 0
    for i in range(len(sol)):
        profit += data['profit'][i]*sol[i]
    return profit



data = {
    'profit': [20, 30, 66, 40, 60],
    'weight': [10, 20, 30, 40, 50],
    'max_weight': 100
    }
sol = greedy_knapsack(data)


print(sol)
cost = calculate_cost(sol,data)
print(cost)