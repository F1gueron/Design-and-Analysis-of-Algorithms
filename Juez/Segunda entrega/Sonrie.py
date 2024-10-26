def best(members, candidates):
    best_ratio = float('inf')
    best_item = -1
    for i in candidates:
        if members[i][1]/members[i][2] < best_ratio:
            best_ratio = members[i][1]/members[i][2]
            best_item = i
    return best_item


def greedy(members):
    n = len(members)
    candidates = set()
    time = 0
    wait = 0
    sol = []
    for i in range(n):
        candidates.add(i)
    while candidates:
        best_candidate = best(members,candidates)
        actual_member = members[best_candidate]
        if best_candidate == 0:
            wait = time
        sol.append(actual_member[0])
        time += actual_member[3]
        candidates.remove(best_candidate)
    return sol, wait

if __name__ == "__main__":
    N = int(input().strip())
    sol = []
    members = []
    for _ in range(N):
        data = input().strip().split()
        name = data[0]
        pacience = int(data[1])
        urgence = int(data[2])
        time = int(data[3])
        members.append([name, pacience, urgence, time])
    members.sort()
    sol, wait = greedy(members)
    for result in sol:
        print(result)
    print(wait)