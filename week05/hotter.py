import sys, heapq
input = sys.stdin.readline

scoville_list = list(map(int, input().rstrip().split()))
K = int(input())


def solution(scoville_list, K):
        
    answer = 0
    heap = []
    
    for scoville in scoville_list:
        if not heap:
            heapq.heappush(heap, scoville)
        else:
            while heap[0] < K: # 힙의 최솟값과 비교 
                if len(heapq) > 1:
                    new_scoville = heapq.heappop[0] + (heapq.heappop[1] *2)
                    heapq.heappush(heap, new_scoville)
                    answer += 1
                else:
                    return -1

    return answer