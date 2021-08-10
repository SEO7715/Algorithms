import sys

N = int(sys.stdin.readline())
numbers = []

for x in range(N):
    tmp = int(sys.stdin.readline())
    numbers.append(tmp)

# (최대)힙 구조 만들기
def heapify():
    for i in range(1, N): #1부터 N-1까지
        c = i # c = i
        while c > 0:
            root = (c - 1) // 2 # 부모 --> 왜 식이 이렇게 되는거지..
            if numbers[c] > numbers[root]: # 자식이 부모보다 클 때
                numbers[c], numbers[root] = numbers[root], numbers[c] # 부모, 자식 위치 변경
            c = root #자식 값 부모한테 주기
    return

# 힙 정렬하기(오름차순)
def heap_sort():
    for i in range(N - 1, -1, -1):  # 위에서부터 아래로 내려오면서 확인
        # 맨 앞과 맨 뒤를 교환! ( 가장 큰 수를 뒤로 보낸다. 그리고 그 가장 큰 수는 FIX )
        numbers[0], numbers[i] = numbers[i], numbers[0]

        # 다시 힙구조로 바꿔주기 # logn
        root, c = 0, 1
        while c < i: # 힙구조는 오름차순 st니깐 내림차순으로 정렬해주기 위함
            c = root * 2 + 1
            if c < i - 1 and numbers[c] < numbers[c + 1]:
                c += 1

            if c < i and numbers[c] > numbers[root]: 
                numbers[c], numbers[root] = numbers[root], numbers[c] 
            root = c 
    return 

heapify()
heap_sort()
print(numbers)