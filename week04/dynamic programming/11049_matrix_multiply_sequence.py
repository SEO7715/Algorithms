import sys
input = sys.stdin.readline

N = int(input()) 
matrices = [None] * N # 각 행렬 정보 내역 받기 위한 리스트

for i in range(N):
    matrices[i] = list(map(int, sys.stdin.readline().split()))
# print(matrices) # [[5, 3], [3, 2], [2, 6]]

dp =[[0] * N for _ in range(N)]  # dp 탐색 위해 초기 설정한 arr 

# print(dp) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for j in range(1, N):
    for i in range(j-1, -1, -1):
        # print(i) # range(j-1, -1, -1)일 경우, 0 1 0
        candidate = sys.maxsize 
        for k in range(i, j):
            candidate = min(candidate 
                            , matrices[i][0] * matrices[k+1][0] * matrices[j][1]
                            + dp[i][k] + dp[k+1][j])
        dp[i][j] = candidate
print(dp[0][N-1])
