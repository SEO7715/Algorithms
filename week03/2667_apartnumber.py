import sys
input = sys.stdin.readline

N  = int(input())
# 단지 리스트
apart_list = [list(map(int, input().strip())) for _ in range(N)]
count = 0
result = []

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

## dfs를 이용하여, 이어진 단지 탐색
def dfs(x, y):
    global count

    if 0 > x or x >= N or 0 > y or y >= N:
        return False

    if apart_list[x][y] == 1:
        count += 1
        apart_list[x][y] = 0 # 중복 count 방지
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        # print(count)
        return True

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(count)
            # print(result) [7], [7, 8], [7, 8, 9]
            count = 0

print(len(result))
result.sort()
for i in result:
    print(i)