n = 45

def solution(n):
    result = []
    answer = 0
    check_n = n
    while check_n != 0:
        rest_n = check_n % 3 
        check_n = check_n // 3 
        result.append(rest_n) 
    N = len(result)
    for i in range(N):
        answer += result[i]*(3**(N-(i+1)))
    return answer


print(solution(n))