import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N+1)])
remove_list = []

while len(queue) > 0:
    queue.rotate(-k + 1)
    remove_list.append(queue.popleft())

print("<" + ", ".join(map(str, remove_list))+ ">") # 3 6 2 7 5 1 4 ---> <3, 6, 2, 7, 5, 1, 4>로 바꿔주기