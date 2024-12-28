from random import randint

def kSmallestElement(k, elements):
    pivot = elements[k]

    low = [x for x in elements if x < pivot]
    if k < len(low):
        return kSmallestElement(k, low)

    k -= len(low)
    equal = [x for x in elements if x == pivot]
    if k < len(equal):
        return pivot

    k -= len(equal)
    high = [x for x in elements if x > pivot]
    return kSmallestElement(k, high)


def median(elements):
    ordinal = (len(elements) - 1) //2
    return kSmallestElement(ordinal, elements)

#kSmallestElement


def test():
    print("Testing ...")
    for _ in range(10000):
        n = randint(1, 100)
        a = [randint(0,99) for i in range(n)]
        copy = a[:]
        #lo particularizamos a la media
        copy.sort()
        expMedian = copy[(len(copy) - 1) // 2]
        med = median(a)
        assert med == expMedian
    print("Done.")

test()
