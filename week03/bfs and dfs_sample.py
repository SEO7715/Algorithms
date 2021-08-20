from collections import deque
import sys
input = sys.stdin.readline

graph = {} #딕셔너리 형태로 그래프 지정
n = input().split()
node, edge, start = [int(i) for i in n]

for i in range(edge):
    edge_info = input().split()
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]: 
        graph[n1].append(n2)
    
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
        
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph: #n이 그래프에 있으면
                temp = list(set(graph[n]) - set(visited)) #그래프 n 집합에서 방문집합을 제외한 내역
                temp.sort(reverse=True) #정렬
                stack += temp #스택에 넣기
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft() #queue의 맨 왼쪽 요소를 뽑아 n에 저장
        if n not in visited:
            visited.append(n)
            if n in graph: 
                temp = list(set(graph[n]) - set(visited)) #그래프 n 집합에서 방문집합을 제외한 내역
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

