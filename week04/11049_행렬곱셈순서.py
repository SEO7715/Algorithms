import sys
input = sys.stdin.readline

N = int(input()) 
matrix = [[0,0]]

for _ in range(N):
    r, c = list(map(int, input().strip().split()))
    matrix.append([r, c])
# print(matrix) # [[0, 0], [5, 3], [3, 2], [2, 6]]

dp =[[0 for _ in range(N)] for _ in range(N+1)]

# print(dp) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue
        if i == j+1:
            dp[i][j] = matrix[j][0] * matrix[j][1] * matrix[i][1]

        # IndexError
        for k in range(j, i-1):
            dp[i][j] = min(dp[i][j],
                            dp[i][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(dp[0][N-1])

