def dfs(graph, start_node):
    need_visited, visited = list(), list()
    # 방문 여부에 따라 각각 리스트 통해 관리(미방문/ 방문)
    need_visited.append(start_node)
    while need_visited: #미방문한 노드가 있는 동안
        node = need_visited.pop()
        # 미방문 리스트 내 가장 마지막 데이터 추출(스택 활용)
        if node not in visited:
            # 해당 노드가 미방문 상태일 경우
            visited.append(node)
            # 방문한 목록에 추가
            need_visited.extend(graph[node])
            #해당 노드에 연결된 자식 노드 미방문 리스트에 추가
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

print(dfs(graph, 'A'))