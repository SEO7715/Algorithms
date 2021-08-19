import sys

N = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []

def solution(x, y, N): # 함수는 x, y를 시작점으로 함. 범위는 N만큼
    color = paper_list[x][y]  
    for i in range(x, x+N): # i라는 변수에 대해서 range 안에 있다. i 는 x부터 x+N까지 있음
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

solution(0, 0, N) #범위의 시작을 0부터 N까지 / (0, 0)을 해도됨
print(result.count(0))
print(result.count(1))
