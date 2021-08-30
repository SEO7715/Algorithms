import sys
input = sys.stdin.readline

import sys
N, M = map(int, sys.stdin.readline().split())

# 속도 j의 값의 상한선이 N값에 달려있으므로
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
# 속도 j값이 최대가 되려면 계속 증가해야 함 1, 2, 3, 4,...j
# 다만, 1부터 j까지의 합이 N이하 여야  마지막 돌을 지나치지 않을 것이므로
# 1부터 j까지의 합은 첫항이 1, 끝항이 j이면서 공차가 1인 등차수열의 합과 동일함
# N >= j(j+1)/2 (j(j+1)/2의 값은 N보다 같거나 작아야 함)
# j의 값이 될 수 있는 경우는 (int((2 * N)** 0.5) + 2)이므로
# 각 지점별(j) dp (int((2 * N)** 0.5) + 2)씩 할당 해주기

# print(dp) # [[inf, inf, inf, inf, inf, inf, inf, inf],...]
dp[1][0] = 0 # 첫번째 돌이 시작점이므로 0으로 설정해주기

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))

for i in range(2, N + 1): # 2부터 N까지
    if i in stone_set: # 작은 돌 예외 처리
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        # dp[i][j]는, i에 도달하기 위해 j 속도로 이동할 경우, 최소한의 점프 횟수
        # j-1, j, j+1 칸 이동했을 경우 중 가장 최소의 경우를 선택

if min(dp[N]) == float('inf'): # N번 돌까지 점프해갈 수 없는 경우
    print(-1)
else: 
    print(min(dp[N]))