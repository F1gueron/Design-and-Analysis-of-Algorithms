def rec_bs(v, number, low, high):
    if low > high:  # caso base
        return -low - 1

    mid = (low + high) // 2
    if v[mid] == number:
        return mid
    elif number < v[mid]:
        return rec_bs(v, number, low, mid - 1)
    else:
        return rec_bs(v, number, mid + 1, high)


def recBinarySearch(v, number):
    return rec_bs(v, number, 0, len(v) - 1)


if __name__ == "__main__" :
    n = int(input())
    group1 = list(map(int, input().split()))
    m = int(input())
    group2 = list(map(int, input().split()))
    p = int(input())
    for _ in range(p):
        p1, p2 = map(int, input().split())
        pos1 = recBinarySearch(group1, p1)
        pos2 = recBinarySearch(group2, p2)
        if pos1 >= 0 and pos2 >= 0:
            print(f"{pos1} {pos2}")
        else:
            print("SIN DESTINO")