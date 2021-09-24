begin = input() 
target = input()
words = list(map(str, input().split()))

def bfs(begin, target, words, visited):
    count = 0
    stack = [begin]
        
    while stack:
        curr = stack.pop()
        if curr == target:
            return count
    
        for i in range(len(words)):
            if visited[i] == True:
                continue
            count_help = 0
            for a, b in zip(curr, words[i]):
                if a != b:
                    count_help += 1
            if count_help == 1:
                visited[i] = True
                stack.append(words[i])
        count += 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [False] * (len(words))
    answer = bfs(begin, target, words, visited)
    return answer

        

print(solution(begin, target, words))