import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline()) 
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_count = 1 
visited = [[False] * n for _ in range(n)]




def dfs(level, x, y):
    global n, maps, visited, dx, dy
    
    # while maps:
    #     spot = maps.pop()
    for i in range(4): 
        nx = x + dx[i] #인접한 영역도 찾아주어야 하므로 방향 설정
        ny = y + dy[i] 

        if (0 <= nx < n and 0 <= ny < n) and (maps[nx][ny] > level) and not (visited[nx][ny]):
            visited[x][y] = True
            dfs(level, x, y)
        return



for level in range(1, 101): 
    count = 0
    for i in range(n): 
        for j in range(n): 
            if maps[i][j] > level and not visited[i][j]: 
                visited[i][j] = True 
                dfs(level, i, j) 
                count += 1 
    if max_count < count: 
        max_count = count

print(max_count)

