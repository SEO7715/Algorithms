import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze_matrix = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(x, y):
    # 방향 설정
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((x,y))
    print(queue) # -> deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for i in range(4): 
            nx = x + dx[i]
            my = y + dy[i]
            if 0 <= nx < n and 0 <= my < m:
                if maze_matrix[nx][my] == 1:
                    maze_matrix[nx][my] = maze_matrix[x][y] + 1
                    queue.append((nx, my))

bfs(0, 0)
# print(maze_matrix[n-1][m-1])
