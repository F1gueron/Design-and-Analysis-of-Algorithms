from random import randint

def partition1(v, left, right):
    pivot = v[left] #pivot = 9
    j = right

    crossed = False
    i = left
    while not crossed:
        crossed = (i > j)
        while v[i] <= pivot and not crossed:
            i += 1
        while v[j] > pivot and not crossed:
            j -= 1
        aux = v[i]
        v[i] = v[j]
        v[j] = aux

    aux = v[j]
    v[j] = v[0]
    v[0] = aux
    return j

def partition(v, left, right):
    pivot = v[left]
    i = left + 1
    while i < right and v[i] <= pivot:
        i += 1

    j = right
    while j > left and v[j] > pivot:
        j -= 1

    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        while v[i] <= pivot:
            i += 1

        j -= 1
        while v[j] > pivot:
            j -= 1

    v[left], v[j] = v[j], v[left]
    return j

def qs_rec(arr, left, right):
    if left > right:
        return arr
    else:
        idx = partition(arr, left, right)
        qs_rec(arr, left, idx - 1)
        qs_rec(arr, idx + 1, right)

def quickSort(elements):
    qs_rec(elements, 0, len(elements) - 1)

#QuickSort_DaC

def test_QuickSort():
    print("Testing ...", end = " ")

    for _ in range(1000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(0,50))
        copy = input[:] #Hago una copia explícita
        quickSort(input)
        copy.sort()
        assert copy == input #verifica que los elementos de input y de copy son los mismo
    print("Done")


test_QuickSort()