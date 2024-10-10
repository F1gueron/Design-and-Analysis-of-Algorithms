def get_best_task(candidates, tasks):
    best_time_task = 0x3f3f3f3f
    best_task = 0
    for c in candidates:
        time = tasks[c]
        if time < best_time_task:
            best_time_task = time
            best_task = c
    return best_task

def order_tasks(tasks):
    candidates = set()
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates:
        best_task = get_best_task(candidates,tasks)
        candidates.remove(best_task)
        sol.append(best_task)
    return sol

def calculate_waiting_time(sol,tasks):
    suma = 0
    cum_tasks = []
    for i in range(len(sol)):
        task = sol[i]
        suma += tasks[task]
        cum_tasks.append(suma)

    return cum_tasks

tasks = [3,5,10]
sol = order_tasks(tasks)
print(sol)
cost = calculate_waiting_time(sol,tasks)
print(cost)