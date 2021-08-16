import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for i in range(1, N+1): #0부터 5까지 범위
    queue.append(i) # +1 해주기 

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())


