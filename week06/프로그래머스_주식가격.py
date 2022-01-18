from collections import deque
prices = [5,5,4,3,2]	

def solution(prices):
    result = []
    q = deque(prices)

    while q:
        tmp = q.popleft()
        count = 0

        for curr in q:
            count += 1
            if curr < tmp:
                break
        result.append(count)
    return result

print(solution(prices))