import sys, heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    number = int(sys.stdin.readline())

    if number != 0:
        heapq.heappush(heap, -number) #힙큐는 최소값 정렬이므로, 역으로(-) 정렬해주기
    else: 
        try:
            print(-1 * heapq.heappop(heap)) 
            #배열에서 가장 큰 값 출력/ 역으로(-) 정렬해줬으므로 (-) 붙인 값으로 출력해야 (+)값 출력됨
        except:
            print(0)
