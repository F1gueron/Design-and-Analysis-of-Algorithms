def rec_bs(v, number, low, high):
    if low > high:
        return -low - 1

    mid = (low + high) // 2

    if v[mid] == number:
        return mid
    elif number < v[mid]:
        return rec_bs(v, number, low, mid - 1)
    else:
        return rec_bs(v, number, mid + 1, high)


def recBinarySearch(v, number):
    print(v)
    print(number)
    return rec_bs(v, number, 0, len(v) - 1)


def clear_souls(levels, cases):
    array_sumas = [0] * len(levels)
    array_sumas[0] = levels[0]
    for i in range(1, len(levels)):
        array_sumas[i] = array_sumas[i - 1] + levels[i]

    results = []

    for knight_level in cases:
        index = recBinarySearch(levels, knight_level)
        print("Index", index)
        if index >= 0:
            enemies_defeated = index + 1
            points = array_sumas[index]
        else:
            index = -index - 1
            enemies_defeated = index
            if index != 0:
                points = array_sumas[index - 1]
            else:
                points = 0

        results.append(f"{enemies_defeated} {points}")

    return results


if __name__ == "__main__":
    n = int(input())
    levels = list(map(int, input().split()))
    m = int(input())
    cases = [int(input()) for _ in range(m)]

    results = clear_souls(levels, cases)
    for answer in results:
        print(answer)
