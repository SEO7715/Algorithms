import sys
input = sys.stdin.readline

N = int(input())
number_list = [list(map(int, input().rstrip())) for _ in range(N)]
result = []

def solution(x, y, N):
    color = number_list[x][y]  
    for i in range(x, x+N): 
        for j in range(y, y+N):
            if color != number_list[i][j]:
                result.append('(')
                solution(x, y, N//2)
                solution(x, y+ N//2, N//2)
                solution(x+ N//2, y, N//2)
                solution(x+ N//2, y + N//2, N//2)
                result.append(')')
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)

print("".join(map(str, result)))
