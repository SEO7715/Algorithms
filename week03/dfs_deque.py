from typing import Collection

def dfs2(graph, start_node):
    from collections import deque

    visited = [] #방문 내역 리스트
    need_visited = deque() #미방문 내역은 deque 활용
    # print(need_visited) --> deque([])

    need_visited.append(start_node) # 시작 노드 설정해주기
    # print(need_visited) --> deque(['A'])

    while need_visited:
        node = need_visited.popleft()
        #시작 노드 지정
        if node not in visited:
            # 해당 노드가 방문 내역에 없을 경우
            visited.append(node)
            # 해당 노드를 방문 내역에 추가
            need_visited.extend(graph[node])
            # 해당 노드의 자식 노드를 미방문 내역에 추가
    return visited

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs2(graph, 'A'))