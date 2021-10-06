
def dfs(computers, visited, check_number):
    if visited[check_number] == 0:
        visited[check_number] = 1
        
    for i in range(len(computers)):
        if computers[check_number][i] == 1 and visited[i] == 0:
            dfs(computers, visited, i)
            
def solution(n, computers):
    visited = [0] * n
    answer = 0
    while 0 in visited:
        for j in range(n):
            if visited[j] == 0:
                dfs(computers, visited, j)
                answer += 1
    return answer