from collections import deque
prices = [5,5,4,3,2]	

# ver1
# def solution(prices):
#     result = []
#     q = deque(prices)

#     while q:
#         tmp = q.popleft()
#         count = 0

#         for curr in q:
#             count += 1
#             if curr < tmp:
#                 break
#         result.append(count)
#     return result



# ver2

def solution(prices):
    N = len(prices)
    idx_stack = []
    result = [0] * N
    for curr_idx in range(N):
        while idx_stack and prices[idx_stack[-1]] > prices[curr_idx]:
            tmp = idx_stack.pop()
            result[tmp] = curr_idx - tmp
        idx_stack.append(curr_idx)

    for i in idx_stack:
        result[i] = (N -1) -i
    return result

print(solution(prices))
