def dfs_recursive(graph, start, visited = []):
    # visited 자료형을 기본 함수 인자로 포함
    visited.append(start)
    # 방문한 리스트를 재귀함수를 통해 visited에 계속 추가
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
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

print(dfs_recursive(graph, 'A'))