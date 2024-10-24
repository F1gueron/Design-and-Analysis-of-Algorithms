def getBestItem(participants, candidates):
    bestAge = float('inf')
    bestItem = float('inf')
    for c in candidates:
        age = participants[c][1]
        if age < bestAge:
            bestAge = age
            bestItem = c
    return bestItem


def greedy(participants, groupSize):
    n = len(participants)
    candidates = set()
    for i in range(n):
        candidates.add(i)
    groupSize = min(n - groupSize,groupSize)
    young = []
    old = []
    for _ in range(groupSize):
        bestPartner = getBestItem(participants,candidates)
        candidates.remove(bestPartner)
        young.append(participants[bestPartner][0])
    while candidates:
        bestPartner = getBestItem(participants, candidates)
        candidates.remove(bestPartner)
        old.append(participants[bestPartner][0])
    print(" ".join(young))
    print(" ".join(old))



if __name__ == "__main__":
    n, groupSize = map(int, input().strip().split())
    participants = []
    for _ in range(n):
       data = input().strip().split()
       name = data[0]
       age = int(data[1])
       participants.append((name, age))

    greedy(participants, groupSize)