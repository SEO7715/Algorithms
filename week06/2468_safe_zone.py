import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


N = int(input())
island_list = []
safe_zone = [] #안전영역 개수 리스트(높이별)

for _ in range(N):
    island_list.append(list(map(int, input().split())))

height = max(map(max, island_list))

def dfs(x, y, h):
    #방향 설정  
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True
    for j in range(4):
        new_x = x + dx[j]
        new_y = y + dy[j]

        if 0 <= new_x < N and 0 <= new_y < N and island_list[x][y] > h and visited[new_x][new_y] == False:
            dfs(new_x, new_y, h)

for i in range(height):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for p in range(N):
        for q in range(N):
            if island_list[p][q] > i and visited[p][q] == False:
                dfs(p, q, i)
                count += 1
                
    safe_zone.append(count)

print(max(safe_zone))



