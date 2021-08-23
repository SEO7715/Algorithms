from collections import deque
import sys
input = sys.stdin.readline

M, N, H = tuple(map(int, input().split()))
matrix = []
frontier = []
goal_count = 0

# 3차원 리스트 만들기
for h in range(H):
    space = []
    for x in range(N):
        row = list(map(int, input().split()))
        space.append(row)
        for y in range(M):
            if row[y] == 1:
                frontier.append((h, x, y))
            elif row[y] == 0: # 안익은 토마토인 경우
                goal_count += 1
    matrix.append(space)

def bfs(matrix, frontier):
    search_count = 0 #방문 해야할 곳
    if goal_count == 0:
        return search_count
    
    max_time = 0
    
    # 방향설정
    dhs = [0, 0, 0, 0, -1, 1]
    dxs = [-1, 1, 0, 0, 0, 0]
    dys = [0, 0, -1, 1, 0, 0]

    frontier = deque(frontier)
    while frontier:
        v1 = frontier.popleft()
        v1_h, v1_x, v1_y = v1
        v1_time = matrix[v1_h][v1_x][v1_y]

        for dh, dx, dy in zip(dhs, dxs, dys):
            h = v1_h + dh
            x = v1_x + dx
            y = v1_y + dy

            if h < 0 or h >= H or x < 0 or x >= N or y < 0 or y >= M:
                continue

            if matrix[h][x][y] != 0:
                continue

            search_count += 1
            matrix[h][x][y] = v1_time + 1
            
            if max_time < v1_time:
                max_time = v1_time

            frontier.append((h, x, y))

    if search_count == goal_count:
        return max_time

    else:
        return -1

print(bfs(matrix, frontier))
