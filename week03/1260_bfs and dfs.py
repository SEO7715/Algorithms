def bfs(graph, start):
    visited = []
    adjacency_nodes = deque([start]) #인접 노드
    
    while adjacency_nodes:
        node = adjacency_nodes.popleft()
        if node not in visited:
            visited.append(node)
            adjacency_nodes.extend(graph[node])
    
    return visited

def dfs_recur(graph, start, visited = []):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recur(graph, node, visited)
    return visited

if __name__ == '__main__':
    from collections import deque
    import sys
    read = sys.stdin.readline

    n, m, v = map(int, read().split()) 
    #n 정점 / m 간선/ v 시작 번호

    graph = [[] for _ in range(n+1)]
    #2차원 배열 만들기/ 인덱스 번호 일치 위해 n+1 숫자 사용

    for _ in range(m): #간선 수 범위 
        a, b = map(int, sys.stdin.readline().strip().split()) 
        # 간선이 연결하는 두 정점 번호
        graph[a].append(b)
        graph[b].append(a)


    print(dfs_recur(graph, v))
    print(bfs(graph, v))
