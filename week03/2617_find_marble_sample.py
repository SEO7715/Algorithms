def dfs(node, weight):
    global count
    visited[node] = True # 방문표시 해주기
    for j in weight[node]: 
        if not visited[j]: # 미방문 상태이면,
            count += 1
            # print(count)
            dfs(j, weight)
    return count

__if__ = '__main__'

N, M = map(int, input().split())

# 역방향 탐색 위한 인접리스트
heavy = [[] for _ in range(N+1)]
# 정뱡향 탐색 위한 인접리스트
light = [[] for _ in range(N+1)]
result = 0

for i in range(M):
    a, b = map(int, input().split())
    heavy[a].append(b) 
    light[b].append(a)

    # print('hhhhh', heavy) # [[], [], [1], [], [3, 2], [1]]
    # print('lllll', light) # [[], [2, 5], [4], [4], [], []]

for i in range(1, N+1):
    visited = [False] * (N+1)
    
    count = 0 # 왜하지,,
    # 무거운 것의 개수가 중간 번호보다 많으면 중간 구슬 될 수 없음
    if dfs(i, heavy) >= (N+1)//2:
        result += 1

    count = 0 # 왜하지,,
    #가벼운 것의 개수가 중간번호보다 많으면 중간 구슬될 수 없음
    if dfs(i, light) >= (N+1)//2:
        result += 1

print(result)