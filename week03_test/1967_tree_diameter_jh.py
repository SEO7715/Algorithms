import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

# inputs
n = int(sys.stdin.readline())
graph = defaultdict(list)
in_degree = defaultdict(int)
for _ in range(n-1):
    num1, num2, weight = map(int, sys.stdin.readline().split())
    graph[num1].append((num2, weight))
    graph[num2].append((num1, weight))
    in_degree[num1] += 1
    in_degree[num2] += 1

one_indegrees = [i for i in in_degree if in_degree[i] == 1] # indgree 1 찾기
start = one_indegrees[0] if one_indegrees else 0            # indexError 방지

def max_diameter(graph, start):

    def _dfs(curr, curr_weight):

        visited[curr] = True
        branches = [0]
        for next, next_weight in graph[curr]:
            if not visited[next]:
                route[0] += next_weight
                branches.append(_dfs(next, next_weight))
                route[0] -= next_weight

        # update
        max_dia[0] = max(max_dia[0], sum(sorted(branches + route[:], reverse=True)[:2]))
        return max(branches) + curr_weight

    if not graph:
        return 0

    visited = defaultdict(lambda: False)
    max_dia = [0]
    route = [0]

    _dfs(start, graph[start][0][1])
    return max_dia[0]

print(max_diameter(graph, start))