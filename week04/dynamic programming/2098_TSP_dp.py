import sys

def go(now, trace): # now는 현재 경유지 번호/ trace는 현재까지 경유지 집합(현재 포함)
    if dp[now][trace]: # dp[now][trace]이 있다면, 해당 값 리턴해주기(중복 체크 방지)
        return dp[now][trace]

    # 기저 조건(V0부터 Vn-1까지 모두 거쳤다는 의미. V0으로 복귀만 남은 상태)
    if trace == (1 << N)-1: 
        # 1을 N만큼 이동 후 -1 해주기 --> 1이 N개만큼 있음 --> (V0부터 Vn-1까지 모두 거쳤다는 의미. V0으로 복귀만 남은 상태)를 의미
        return path[now][0] if path[now][0] > 0 else MAX 
        # 현재 경로에서 0으로 가는 비용이 있으면 해당 값 리턴, 없으면 max값으로 설정

    # 각 상태에서 구해야하는 값
    cost = MAX # 비용 최대값으로 설정
    for i in range(1, N): # 1부터 N-1까지
        if not trace & (1 << i) and path[now][i]:
            # trace(현재까지 경유지 집합)에 i가 없고, now에서 i로 가는 비용이 0이 아닐 때(갈 수 있는 경로일 때)
            # 즉, 도시 i가 trace에 없고, 갈 수 있는 경로일 때
            val = go(i, trace | (1 << i)) # 현재위치는 i로 설정, 현재까지 경유지 집합에 i도시를 포함
            cost = min(cost, val+path[now][i])
            # cost값과 val+path[now][i] 중 최솟값
            # val은 0에서 trace라는 경로를 거쳐 now까지 왔을 때, 최소 비용
            # path[now][i]는 now에서 i로 이동한 비용 

    # dp에 값 갱신
    dp[now][trace] = cost # 현재위치에서, 현재를 포함한 경유지까지 이동하는 최소 비용 cost 값을 dp[now][trace]에 넣기 
    return dp[now][trace] # dp[now][trace] 값 리턴

N = int(input())
path = [list(map(int, input().split())) for _ in range(N)] # 도시 간 이동 비용 input값 받기 

dp = [[0] * (1 << N) for _ in range(N)] 
# print(dp) # N을 2진수로 변환하면 2^N 이니깐, 2^4 = 16
MAX = sys.maxsize

print(go(0, 1)) # go(0, 1) = go(0, {1})
# 0 위치에서 시작, 1을 0만큼 이동한 상태