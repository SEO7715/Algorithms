import sys

def go(now, trace):
    if dp[now][trace]:
        return dp[now][trace]

    # 기저 조건
    if trace == (1 << N)-1:
        return path[now][0] if path[now][0] > 0 else MAX

    # 각 상태에서 구해야하는 값
    cost = MAX
    for i in range(1, N):
        if not trace & (1 << i) and path[now][i]:
            val = go(i, trace | (1 << i))
            cost = min(cost, val+path[now][i])

    # dp에 값 갱신
    dp[now][trace] = cost
    return dp[now][trace]

N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)] 
# print(dp) # N을 2진수로 변환하면 2^N 이니깐, 2^4 = 16
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

MAX = sys.maxsize

print(go(0, 1))