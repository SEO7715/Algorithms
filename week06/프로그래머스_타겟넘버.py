def solution(numbers, target):

    def dfs(level, total):

        if level > len(numbers) - 1: # level = 5
            if total == target:
                count[0] += 1
            return 
            
        for sign in [1, -1]:
            dfs(level+1, total + sign*numbers[level])

    count = [0]
    dfs(0, 0)

    return count[0]

