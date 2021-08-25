from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N 수빈이 위치, K 동생 위치
max = 100001
visited = [0] * max
q = deque()
q.append((N, 0))

while q:
    now = q.popleft()
    if now[0] == K:
        print(now[1])
        break
    for next in [now[0]-1, now[0]+1, 2*now[0]]:
        if 0 <= next < max and visited[next] == 0:
            visited[next] = 1 # 방문 표시
            if next == now[0]-1 or next == now[0]+1: # x-1, x+1 일때는 1초의 시간을 증가시켜 데크의 뒤쪽
                q.append((next, now[1]+1))
            if next == 2*now[0]: # 2*x인 경우에는 시간이 걸리지 않으므로 데크의 앞쪽
                q.appendleft((next, now[1]))