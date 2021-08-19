def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1 #방문했으면, 1
    while q: #q가 있는동안
        v = q.popleft() 
        print(v, end=" ")
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1: #미방문 상태이고, 간선으로 연결됨
                q.append(i)
                visit_list[i] = 1 #방문했으면, 1로 표시

def dfs(v):
    visit_list2[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

if __name__ == '__main__':

    from collections import deque
    import sys
    read = sys.stdin.readline

    n, m, v = map(int, read().split()) #n 정점 / m 간선/ v 시작 번호

    graph = [[0] * (n + 1) for _ in range(n+1)] #왜지..?
    visit_list = [0] * (n + 1) #미방문 = 0
    visit_list2 = [0] * (n + 1)

    for _ in range(m): #간선 수 범위 
        a, b = map(int, read().split()) #간선이 연결하는 두 정점 번호
        graph[a][b] = graph[b][a] = 1

    dfs(v)
    print()
    bfs(v)