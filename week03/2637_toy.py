import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
link = [[] for _ in range(n+1)]
matrix = [[0]*(n+1) for _ in range(n+1)]
# print(matrix)
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
        # print('****************************', link[now]) [(5, 2)]
        if matrix[now].count(0) == n+1: # [0, 0, 0, 0, 0, 0, 0, 0]
            print(matrix[now])
            print('****************************', matrix[next])
            matrix[next][now] += needs
            print(matrix[next][now])
        else:
            for i in range(1, n+1):
                matrix[next][i] += matrix[now][i]*needs
                # print(matrix[next][i])
        indegree[next] -= 1
        if indegree[next] == 0:
            que.append(next)
            # print(que)

for i in enumerate(matrix[n]):
    if i[1] > 0:
        print(*i)
