import sys

array = list(map(int, sys.stdin.readline().split()))

def Qsort (array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    left = []
    right = []

    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return Qsort(left) + [pivot] + Qsort(right)

# print(Qsort(array))

for i in array:
    print(Qsort(set(array)))
    