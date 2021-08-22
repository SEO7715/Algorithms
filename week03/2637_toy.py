import sys
from collections import deque
from types import resolve_bases
input = sys.stdin.readline

n = int(input())
m = int(input())
link = [[] for _ in range(n+1)]
matrix = [[0]*(n+1) for _ in range(n+1)]
indegree = [0] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    link[b].append((a, c))
    indegree[a] += 1

que = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    for next, needs in link[now]:
        if matrix[now].count(0) == n+1:
            matrix[next][now] += needs
        else:
            for i in range(1, n+1):
                matrix[next][i] += matrix[now][i]*needs
        indegree[next] -= 1
        if indegree[next] == 0:
            que.append(next)

for i in enumerate(matrix[n]):
    if i[1] > 0:
        print(*i)
