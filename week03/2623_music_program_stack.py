# using dfs(recursion)
def music_dfs(N, graph, in_degree):

    def _dfs(curr):

        # 순환구조시 탐색 안함
        if has_cycle[0]:
            return

        visited[curr] = True
        # 현재까지의 경로 기록
        route.append(curr)

        for next in graph[curr]:
            # 순환구조 판단
            if next in route:
                has_cycle[0] = True
            if not visited[next]:
                _dfs(next)
        # 노드 탐색 완료시 경로에서 pop하고, result에 추가
        route.pop()
        result.append(curr)

    visited = [False] * (N+1)   # 노드 방문 여부 기록
    route = []                  # 탐색 경로 기록
    has_cycle = [False]         # 순환구조여부 파악
    result = []                 # 수행 결과를 담을 리스트
    
    for node in range(N+1):
        if not in_degree[node]: # 진입차수 0인 노드 탐색 
            _dfs(node)

    if has_cycle[0]:            # 순환구조시 0 출력
        print(0)
    else:                        # 역순으로 출력
        print(*result[-1:-N-1:-1], sep='\n')
    return 

#########################################################
__if__ = '__main__'

from collections import defaultdict
import sys
input = sys.stdin.readline

# inputs
N, M = map(int, sys.stdin.readline().split()) 
graph  = defaultdict(list) # defaultdict(<class 'list'>, {})
# print(graph)
in_degree = [0] * (N+1) # 진입차수 0으로 초기화

for _ in range(M):
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1, nums[0]):
        in_degree[nums[i+1]] += 1
        graph[nums[i]].append(nums[i+1])

music_dfs(N, graph, in_degree)