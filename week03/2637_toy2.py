# 출력값 안나옴- 다시 확인 필요
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
indegree = [0] * 101
v = [[0]* (n+1) for _ in range(n+1)]

for i in range(m):
    cur, prev, val = map(int, input().split())
    graph[prev].append((cur, val))
    indegree[cur] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        v[i][i] == 1

while q:
    now = q.popleft()
    for next in graph[now]:
        for i in range(1, n+1):
            v[next[0]][i] += next[1]*v[now][i]
        indegree[next[0]] -= 1
        if indegree[next[0]] == 0:
            q.append(next[0])

for i in range(1, n+1): # 1부터 n까지
    if v[n][i]:
        print(f"{i} {v[n][i]}")



