import sys
from collections import deque
  
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
 
need_parts = [[] for row in range(N+1)]
parts_needed = [0]*(N+1)
EA_list = [0]*(N+1)
# print(EA_list) [0, 0, 0, 0, 0, 0, 0, 0]
visited = [0]*(N+1)
basic = []

for m in range(M):
    x, y, EA = map(int,sys.stdin.readline().split())
    need_parts[x].append([y,EA])
    parts_needed[y] += 1
    # print(parts_needed[y]) # 카드별 사용된 횟수 만큼 카운트 ex. 1번카드 1번, 5번 카드 2번 

while sum(parts_needed) > 0:

    for i in range(1, N+1):
        # print(EA_list[i])
        if not need_parts[i] and visited[i] == 0: # 기본 부품이고, 미방문 상태인 경우
            basic.append(i)
            # print(basic) --> [1, 2, 3, 4]
            visited[i] = 1
        print(EA_list[i])

        if parts_needed[i] == 0 and visited[i] == 0: # 진입 차수가 0이고, 미방문 상태인 경우
            # print(EA_list[i])
            if EA_list[i] == 0:
                EA_list[i] = 1
            visited[i] = 1

            for j in need_parts[i]:
                EA_list[j[0]] += j[1]*EA_list[i] 
                parts_needed[j[0]] -= 1


for i in basic:
    print(i, EA_list[i], sep=" ")