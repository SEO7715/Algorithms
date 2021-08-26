import sys
input = sys.stdin.readline

N = int(input())
apartment_list = [list(map(int, input().strip())) for _ in range(N)]
count = 0
result = []

# 방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    
    if x < 0 or x >= N or y < 0 or y >= N: # 범위 내 존재 여부 확인
        return False
    
    if apartment_list[x][y] == 1:
        count += 1
        apartment_list[x][y] = 0 # 중복 count 방지
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            dfs(new_x, new_y)
        return True

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(count)
            count = 0
            
result.sort()
print(len(result))

for i in result:
    print(i)