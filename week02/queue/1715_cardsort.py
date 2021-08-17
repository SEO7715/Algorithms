import sys, heapq
input = sys.stdin.readline

n = int(input())
number_list = []

for _ in range(n):
    number = int(input())
    number_list.append(number)

heapq.heapify(number_list)
result = 0
while len(number_list) > 1:
    a = heapq.heappop(number_list)
    b = heapq.heappop(number_list)
    heapq.heappush(number_list, a + b)
    result += a + b

print(result)

