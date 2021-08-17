import sys, heapq
input = sys.stdin.readline

max_heap = []
min_heap = []

n = int(input())
for _ in range(n):
    number = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-number, number)) # 최댓값 정렬
    else:
        heapq.heappush(min_heap, (number, number)) 

    if min_heap and max_heap[0][1] > min_heap[0][1]: 
        # min_heap(최소값 모음)에 있으면서, max_heap[0](최대값의 가장 큰 수) 보다 큰 경우: 원칙에 어긋나므로 바꿔주기
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (max_value, max_value))
        heapq.heappush(max_heap, (-min_value, min_value))

    print(max_heap[0][1])
    


