import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    value  = sys.stdin.readline().split()

    if value[0] == 'push':
        queue.append(value[1])

    elif value[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif  value[0] == 'size':
        print(len(queue))
    
    elif value[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif value[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif value[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)