from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

total = 0
for j in range(N):
    total += sum(graph[j])
if total == M * N:
    print(0)
    exit()

time = 0
q = deque()
for y in range(M):
    for x in range(N):
        if graph[x][y] == 1:
            q.append([x, y, 0])

while q:
    a, b, time_case = q.popleft()
    time = max(time, time_case)
    dir_a = [-1, 0, 1, 0]
    dir_b = [0, -1, 0, 1]
    for i in range(4):
        new_a = a + dir_a[i]
        new_b = b + dir_b[i]

        if 0 <= new_a < N and 0 <= new_b < M and graph[new_a][new_b] == 0:
            graph[new_a][new_b] = 1
            q.append([new_a, new_b, time_case + 1])

valid_check = True

for i in range(N):
    if 0 in graph[i]:
        valid_check = False

if valid_check == True:
    print(time)
else:
    print(-1)

