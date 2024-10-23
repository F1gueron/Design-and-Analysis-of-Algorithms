
def getBestTask(candidates, tasks):
    bestTimeTask = 0x3f3f3f
    bestTask = 0
    for c in candidates:
        time = tasks[c]
        if time < bestTimeTask:
            bestTimeTask = time
            bestTask = c
    return bestTask


def orderTasks(tasks):
    candidates = set()
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates:
        bestTask = getBestTask(candidates, tasks)
        candidates.remove(bestTask)
        sol.append(bestTask)
    return sol

def calculateWaitingTime(sol,tasks):
    array = []
    suma = 0
    for i in range(len(sol)):
        task=sol[i]
        suma += tasks[task]
        array.append(suma)
    print(sum(array))

#Main prog.
tasks = [5,10,3]
print(tasks)
sol = orderTasks(tasks)
print(sol)
calculateWaitingTime(sol,tasks)





