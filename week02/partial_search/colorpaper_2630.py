import sys

N = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []

def solution(x, y, N):
    color = paper_list[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper_list[i][j]:
                solution(x, y, N//2)
                solution(x, y+ N//2, N//2)
                solution(x+ N//2, y, N//2)
                solution(x+ N//2, y + N//2, N//2)
                return #함수종료
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))
