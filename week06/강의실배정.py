import heapq
import sys 
input = sys.stdin.readline

N = int(input())

class_list = [] 
room_list = []

for _ in range(N):
    class_list.append(list(map(int, input().split())))

class_list.sort(key=lambda x:x[0])

for _class in class_list:
    if len(room_list) == 0:
        heapq.heappush(room_list, _class[1])
        
    else:
        if room_list[0] > _class[0]: 
            heapq.heappush(room_list, _class[1])
        else:
            heapq.heappop(room_list)
            heapq.heappush(room_list, _class[1])
