import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
MAX = 10001 # N(2 ≤ N ≤ 10,000)개 이므로
dp = [[-1]*150 for i in range(MAX)] 
# dp 초기값 -1 설정,, 0이나 1은 쓰이는 값이므로 사용하지 않을 -1 로 해주는 것
# 또한, N(2 ≤ N ≤ 10,000)개 기준으로 계산해서 150개 메모리 할당

ch = [0 for i in range(N+1)] ## 작은 돌 표시 위한 배열
flag = False 

for i in range(M): # 작은 돌 입력 
    idx = int(input())
    ch[idx] = 1 #방문표시 해주기(방문할 수 없으므로)

def go(idx, jump): #dfs 탐색 / 중복 방문 방지를 위해 dp에 저장해주기
    global flag
    if idx == N: # idx는 모든 돌 위치/ 현재 돌 위치가 최종 돌 위치에 도달했다면
        flag = True # flag는 True로 바꿔주기
        return 0

    if dp[idx][jump] != -1:
        return dp[idx][jump]

    dp[idx][jump] = sys.maxsize
    for i in range(-1, 2): # -1, 0, 1  # x-1칸 또는 x칸 또는 x+1칸 이동하므로
        if jump+i >= 1: # 1이상이어야 앞으로 이동할 수 있음
            next = idx+(jump+i) # next는 현재 위치에서 이동한 만큼(jump+i) 더해준 위치
            if next <= N and ch[next] != 1: # 범위 내 있고, 작은 돌이 아니라면
                dp[idx][jump] = min(dp[idx][jump], 1+go(next, jump+i))

    return dp[idx][jump]

res = go(1, 0)

if flag: # flag값이 True
    print(res) 
else: # flag값이 False면 도달하지 못한 것이므로
    print(-1)