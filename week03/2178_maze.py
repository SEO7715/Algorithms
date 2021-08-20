from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze_list = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze_list[nx][ny] == 1:
                    maze_list[nx][ny] = maze_list[x][y] + 1
                    queue.append((nx, ny))
    

bfs(0,0)
print(maze_list[n-1][m-1])
