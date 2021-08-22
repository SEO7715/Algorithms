import sys
from collections import deque
  
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
 
need_parts = [[] for row in range(N+1)]
parts_needed = [0]*(N+1)
EA_list = [0]*(N+1)
visited = [0]*(N+1)
basic = []

for m in range(M):
    x, y, EA = map(int,sys.stdin.readline().split())
    need_parts[x].append([y,EA])
    parts_needed[y] += 1

while sum(parts_needed) > 0:
 
    for i in range(1,N+1):
        if not need_parts[i] and visited[i] == 0:
            basic.append(i)
            visited[i] = 1
      
        if parts_needed[i] == 0 and visited[i] == 0:
            if EA_list[i] == 0:
                EA_list[i] = 1
            visited[i] = 1
 
            for j in need_parts[i]:
                EA_list[j[0]] += j[1]*EA_list[i]
                parts_needed[j[0]] -= 1
 
 
for i in basic:
    print(i, EA_list[i], sep=" ")