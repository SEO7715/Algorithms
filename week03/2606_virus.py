import sys
input = sys.stdin.readline

computer_n = int(input()) #n
computer_connect = int(input()) #edge

computer_matrix = [[] for _ in range(computer_n + 1)]

for i in range(computer_connect):
    a, b = map(int, input().split())
    computer_matrix[a].append(b)
    computer_matrix[b].append(a)

def virus_check(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            virus_check(graph, node, visited)
    return visited

print(len(virus_check(computer_matrix, 1, [])) - 1)