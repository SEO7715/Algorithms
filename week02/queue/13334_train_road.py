import sys, heapq
input = sys.stdin.readline

n = int(input())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

road_limit = int(input())

roads = []

for road in road_info:
    house, office = road
    if abs(house - office) <= road_limit:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:(x[1])) 

answer = 0
heap = [] 
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - road_limit: # 힙의 최솟값과 비교 
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
