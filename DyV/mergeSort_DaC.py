from random import randint




#mergeSort_DaC

def merge(first, second, output):
    f = s = k = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1

    r = f if s == len(second) else s
    remainder = first if s == len(second) else second

    for i in range(r, len(remainder)):
        output[k] = remainder[i]
        k += 1

def mergeSort(elements):
    if len(elements) < 2:
        #Dividir hasta tamaño 1 es un caso teórico. Lo habitual es dividir hata un tamaño
        #mayor para utilizar un método iterativo (como la burbuja)
        return
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, elements)

def test_MergeSort():
    print("Testing ...", end = " ")

    for _ in range(1000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(-50,50))
        copy = input[:] #Hago una copia explícita
        mergeSort(input)
        copy.sort()
        assert copy == input #verifica que los elementos de input y de copy son los mismo
    print("Done")


test_MergeSort()