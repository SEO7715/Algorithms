import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input()) # 노드 개수
nodes = [[] for _ in range(N+1)] 
# N+1개가 되어야 실제 번호랑 인덱스 번호가 일치됨
parents = [0 for _ in range(N+1)] # 부모 노드 저장
# N+1개가 되어야 실제 번호랑 인덱스 번호가 일치됨

# 트리 구조 입력
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def DFS(start, nodes, parents):
    for i in nodes[start]: #노드의 시작지점
        if parents[i] == 0:
            parents[i] = start
            DFS(i, nodes, parents)

DFS(1, nodes, parents)

for i in range(2, N+1):
    print(parents[i])


