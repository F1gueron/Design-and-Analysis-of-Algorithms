def rec_bs(v, number, low, high):
    if low > high: #caso base
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


#BinSearch_DaC

v = [1, 3, 3, 5, 6, 7, 9]

number = 4
index = recBinarySearch(v, number)

if index >= 0:
    print("Element", v[index], " found at pos.", index)
else:
    index = -index - 1
    print("Should be at pos. ", index, "after elemeent", v[index])



