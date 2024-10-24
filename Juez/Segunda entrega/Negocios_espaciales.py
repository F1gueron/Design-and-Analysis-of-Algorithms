def changeable(n, smallCoin):
    return n >= smallCoin


def greedy(n, monedas):
    change = [0] * len(monedas)

    for i in range(len(monedas)-1, -1, -1):
        while changeable(n, monedas[i]):
            n -= monedas[i]
            change[i] += 1

    total = sum(change)
    return total, change


if __name__ == "__main__" :
    n = int(input().strip())
    monedas = list(map(int,input().strip().split()))
    monedas.sort()
    total, change = greedy(n,monedas)
    print(total)
    for i in range(len(monedas) - 1, -1, -1):
        if change[i] > 0:
            print(f"{monedas[i]}: {change[i]}")
