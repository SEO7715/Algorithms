import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

# inputs
def max_diameter():

    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    max_dia = [0]

    for _ in range(n-1):
        parent_node, child_node, weight = map(int, sys.stdin.readline().split())
        graph[parent_node].append((child_node, weight)) # 단방향


    def _dfs(curr, curr_weight):

        sub_length = [0]
        for next, next_weight in graph[curr]:
            sub_length.append(_dfs(next, next_weight))

        # update
        sub_length.sort(reverse=True)
        max_dia[0] = max(max_dia[0], sum(sub_length[:2])) 
        # 구한 길이 중 가장 긴 첫번째, 두번째 길이의 합과 현재 max 값 중 비교하여 max 값 갱신 
        return sub_length[0] + curr_weight # '가장 긴 거리 + 가중치' 반환

    _dfs(1, 0)
    return max_dia[0]

print(max_diameter())
