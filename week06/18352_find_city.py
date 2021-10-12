from collections import deque
import sys
input = sys.stdin.readline

city_number, edge, given_dist, start = map(int, input().split())
graph = [[] for _ in range(city_number+1)]
visited = [False] * (city_number + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start, dist):
    visited[start] = True # 첫 시작지점 방문표시 해주기
    q = deque([(start, 0)])
    answer = []
    while q:
        city, dist = q.popleft()
        if dist == given_dist:
            answer.append(city)
            continue
        for next in graph[city]:
            if visited[next] == False:
                visited[next] = True
                q.append([next, dist+1])
    if len(answer) == 0:
            print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(start, 0)