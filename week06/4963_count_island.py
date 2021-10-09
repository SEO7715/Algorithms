import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

## dfs를 이용하여, 이어진 섬 탐색
def dfs(x, y):
    #방향 설정
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    
    island[x][y] = 0 #방문표시용
    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]

        # 범위 내 있고, 해당 좌표 값이 양수인 경우,  
        if 0 <= new_x < h and 0 <= new_y < w and island[new_x][new_y] == 1:
                dfs(new_x, new_y)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [] #섬 리스트
    count = 0
    for _ in range(h):
        island.append(list(map(int, sys.stdin.readline().strip().split())))


    for p in range(h): 
        for q in range(w): 
            if island[p][q] == 1:
                dfs(p, q) 
                count += 1 

    print(count)