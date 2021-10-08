import sys
sys.setrecursionlimit(10000)
from collections import defaultdict

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)] # [[], [], [], [], [], [], []]
visited = [False] * (node + 1) # [False, False, False, False, False, False, False]
count = 0 

# 간선 연결
for _ in range(edge):
    number_a, number_b = map(int, sys.stdin.readline().split())
    graph[number_a].append(number_b)
    graph[number_b].append(number_a)

# print(graph) # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def dfs_recursive(v):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs_recursive(node)
            print(visited)

for i in range(1, node+1):
    if not visited[i]:
        dfs_recursive(i)
        count += 1

print(count)