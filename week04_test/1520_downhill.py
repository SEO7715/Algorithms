# 실패
import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split()) # M 세로, N 가로
downhill_list = [list(map(int, input().strip().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

# 방향 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y):
    if x == N-1 and y == M-1: # 종점에 도달한 경우
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0 # check
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 > new_x or new_x >= N or 0 > new_y or new_y >= M:
            continue

        if downhill_list[new_x][new_y] < downhill_list[x][y]: # 이동 가능 여부 확인
            # IndexError: list index out of range 해결하기
            dp[x][y] += dfs(new_x, new_y)

    return dp[x][y]

print(dfs(0, 0))