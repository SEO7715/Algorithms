import sys
input = sys.stdin.readline

N = int(input())
wine_list = [0] * N
dp = [0] * N
for i in range(N):
    wine_list[i] = int(input())

try: 
    dp[0] = wine_list[0]
    dp[1] = dp[0] + wine_list[1]
    dp[2] = max(dp[1], wine_list[0]+wine_list[2], wine_list[1] + wine_list[2])


    for i in range(3, N):
        dp[i] = max((dp[i-3] + wine_list[i-1] + wine_list[i]), (dp[i-2] + wine_list[i]), dp[i-1])

except:
    pass

print(max(dp))