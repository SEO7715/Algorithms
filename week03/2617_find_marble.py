def dfs(node, weight):
    global count
    visited[node] = True
    for j in weight[node]:
        if not visited[j]:
            count += 1
            dfs(j, weight)
    return count

__if__ = '__main__'

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #n 구슬 개수 / m 구슬 쌍 개수

# 탐색 위한 리스트
heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    heavy[a].append(b)
    light[b].append(a)


for i in range(1, N+1):
    visited = [False] * (N+1)
    print(visited)

    count = 0

    if dfs(i, heavy) >= (N+1)//2:
        result += 1

    count = 0
    if dfs(i, light) >= (N+1)//2:
        result += 1

print(result)
