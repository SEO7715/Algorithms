computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
N = 3

# def solution(n, computers):

def solution(N, computers):
    visited = [False] * N
    count = 0
    
    def dfs(start):
        if not visited[start]:
            visited[start] = True

            for next in range(N):
                if computers[start][next] == 1:
                    dfs(next)
    
    for i in range(N):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

print(solution(N, computers))
