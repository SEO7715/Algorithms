import sys

N = int(sys.stdin.readline())
numbers = []

for x in range(N):
    tmp = int(sys.stdin.readline())
    numbers.append(tmp)

def heapify():
    for i in range(1, N):
        c = i 
        while c > 0:
            root = (c - 1) // 2 
            if numbers[c] > numbers[root]: 
                numbers[c], numbers[root] = numbers[root], numbers[c]
            c = root 
    return

def heap_sort():
    for i in range(N - 1, -1, -1): 
        numbers[0], numbers[i] = numbers[i], numbers[0]

        root, c = 0, 1
        while c < i: 
            c = root * 2 + 1
            if c < i - 1 and numbers[c] < numbers[c + 1]:
                c += 1

            if c < i and numbers[c] > numbers[root]: 
                numbers[c], numbers[root] = numbers[root], numbers[c] 
            root = c 
    return 

heapify()
heap_sort()

for i in numbers:
    print(i)

