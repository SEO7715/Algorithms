import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
tree = defaultdict(list)
answer = 0

# 간선 연결
for _ in range(n-1):
    parent_node, childe_node, distance = map(int, sys.stdin.readline().split())
    tree[parent_node].append((childe_node, distance))

def solve(node, distance):
    if not tree[node]:
        return distance
    total = 0
    m = 0
    for next_node, w in tree[node]:
        m = solve(next_node, distance + w)
        if total < m:
            total = m
    
    return total

for node in range(n):
    tmp = []
    for childe_node, distance in tree[node]:
        tmp.append(solve(childe_node, distance))
    
    tmp.sort(reverse=True)
    total = sum(tmp[:2])
    if answer < total: answer = total

print(answer)