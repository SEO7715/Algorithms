N = 15
def solution(N):
    answer = 0
    for i in range(1, N+1):
        sum_j = 0
        print('i', i)
        for j in range(i, N+1):
            print('j', j)
            if sum_j < N:
                sum_j += j
                print('sum_j', sum_j)
            if sum_j == N :
                answer += 1
                break
            if sum_j > N:
                break
    return answer

print(solution(N))