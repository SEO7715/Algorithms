graph = {0 : [1, 4], 1 : [2, 3], 2 : [1], 3 :[1], 4 : [5], 5 : [4]}
visited = [False for _ in range(len(graph.keys()))]
# visited2 = [False] * len(graph.keys())
print(visited)

start = 0

def dfs(node, level):
    if level > 1:
        return

    if not visited[node]:
        visited[node] = True
        print(node)
        for next in graph[node]:
            dfs(next, level+1)

print(dfs(start, 0))