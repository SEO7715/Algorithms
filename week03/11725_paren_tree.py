import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

nodes = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)] 

for i in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(start):
    for i in nodes[start]: #시작 노드에 있는 i 에 대하여
        if parents[i] == 0: # 부모 노드 i의 값이 0인 경우, 
            parents[i] = start # 부모 노드 i의 값이 시작 지점이 됨
            print(i, start)
            dfs(i) # 해당 노드를 시작지점으로 함수 호출
dfs(1)

for i in range(2, N+1):
    print(parents[i])

