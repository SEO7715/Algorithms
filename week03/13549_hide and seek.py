from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max = 100001
visited = [0] * max
q = deque()
q.append((N, 0)) # 현재 0초

while q:
    now = q.popleft()
    if now[0] == K: # 현재 수빈 위치 = 동생 위치일 경우 종료
        print(now[1])
        break
    else:
        for next in [now[0] - 1, now[0] + 1, 2*now[0]]:
            if 0 <= next < max and visited[next]==0:
                visited[next] = 1
                if next == now[0] - 1 or next == now[0] + 1:
                    q.append((next, now[1] + 1)) #데크 뒤에 넣어주기
                if next == 2*now[0]:
                    q.appendleft((next, 0)) #데크 앞쪽에 넣어주기
