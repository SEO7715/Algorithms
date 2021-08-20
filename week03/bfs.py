def bfs(graph, start_node):
    need_visited, visited = [], []
    # 미방문, 방문 리스트 각각 생성
    need_visited.append(start_node)
    # 미방문 리스트에 시작 노드 추가
    # print(need_visited) --> ['A']
    while need_visited:
        node = need_visited[0]
        # 미방문 리스트의 첫번째 인자 추출
        # print(node)
        # print(need_visited)
        del need_visited[0]
        # print(need_visited)
        if node not in visited:
            visited.append(node)
            # print(visited)
            # 해당 노드 방문 내역에 추가
            need_visited.extend(graph[node])
            print(need_visited)
            #해당 노드의 자식 노드 미방문 내역에 추가
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

print(bfs(graph, 'A'))

