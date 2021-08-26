# 실패
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max = 100001 # 최댓값 설정
visited = [0] * max # 방문 내역 0으로 초기화
q = deque()
q.append((N, 0)) # 현재 상태 q에 넣기

while q:
    now = q.popleft() 
    if now[0] == K:
        print(now[1])
        break
    
    for next in [now[0]-1, now[0]+1, 2*now[0]]:
        if 0 <= next < max and visited[next] == 0:
            visited[next] = 1
            if next == now[0] - 1 or next == now[0] + 1: # +1 또는 -1 은 1초 후 이동
                q.append((next, now[1] + 1))
            if next == 2*now[0]: # 순간이동 
                q.append((next, now[1] + 1))
