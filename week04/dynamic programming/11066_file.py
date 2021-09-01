import sys
input = sys.stdin.readline

test_case = int(input()) 

for i in range(test_case):
    number = int(input())
    number_list = list(map(int, input().strip().split()))


    dp =[[0] * number for _ in range(number)]  # dp 탐색 위해 초기 설정한 arr 

    for j in range(1, number):
        for i in range(j-1, -1, -1):
            dp[i][j] = sys.maxsize 
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
            print(sum(number_list[i:j+1]))
            dp[i][j] += sum(number_list[i:j+1]) 
            # number_list = [40, 30, 30, 50]일 때, dp[0][3] 값을 구하려 할 경우,
            # dp[0][3] 값에 40+30+30+50 값 누적해서 더해주기

    print(dp[0][number-1])