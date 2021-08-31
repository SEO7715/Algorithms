import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

dp = [0] * n
# print(dp)  # [0, 0, 0, 0, 0, 0]

for i in range(n):
    # print(length[i]) # 0 0 0 0 0
    # print(i)  # i는 0, 1, 2, 3, 4, 5
    dp[i] = 1 # 초기 길이값 1로 설정
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    print(dp[i])
print(max(dp))