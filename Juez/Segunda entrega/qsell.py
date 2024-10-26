
def best(partners, candidates,attractive):
    best_ratio = -1
    best_candidate = -1
    for i in candidates:
        if partners[i][attractive]/partners[i][4] > best_ratio:
            best_ratio = partners[i][attractive]/partners[i][4]
            best_candidate = i
    return best_candidate

def notOut():
    pass


def greedy(concursante):
    n = concursante[2]
    candidates = set()
    time_left = concursante[1]
    sol = []
    benefit = 0
    if concursante[0] == "beauty":
        attractive = 1
    elif concursante[0] == "intelligence":
        attractive = 2
    elif concursante[0] == "kindness":
        attractive = 3
    else:
        print("Error")
        attractive = None
    for i in range(n):
        candidates.add(i)
    while candidates and time_left > 0:
        best_candidate = best(concursante[3],candidates,attractive)
        actual_partner = concursante[3][best_candidate]
        if time_left >= actual_partner[4]:
            time_left -= actual_partner[4]
            benefit += actual_partner[attractive]
        else:
            ratio = time_left / actual_partner[4]
            time_left = 0
            benefit += ratio * actual_partner[attractive]
        sol.append(actual_partner[0])
        candidates.remove(best_candidate)

    return sol,benefit




if __name__ == "__main__":
    N = int(input().strip())
    concursante = []
    sol = []
    for i in range(N):
        important_caracteristic = input().strip()
        time_left = int(input().strip())
        tentations = int(input().strip())
        partners = []
        for _ in range(tentations):
            data = input().strip().split()
            name = data[0]
            beauty = int(data[1])
            intelligence = int(data[2])
            kindness = int(data[3])
            time = int(data[4])
            partners.append([name, beauty, intelligence, kindness, time])
        concursante.append([important_caracteristic, time_left, tentations, partners])
        lovers, benefit = greedy(concursante[i])
        sol.append([lovers,benefit])
    for result in range(len(sol)):
        for lover in sol[result][0]:
            print(lover, end=" ")
        print()
        print(f"{sol[result][1]:.2f}")