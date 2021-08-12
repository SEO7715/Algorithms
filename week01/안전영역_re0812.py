import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline()) #행과 열의 개수
case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #위치별 점수 리스트
max_count = 0

def dfs(x, y, level):
    check[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1): #열, 행방향
        nx, ny = x +dx, y +dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n: #nx, ny가 주어진 행과 열을 초과한다면, pass하라는 의미
            continue 
        if not check[nx][ny] and case[nx][ny] > level: # 미방문 + 안잠긴 상태
            dfs(nx, ny, level)

for k in range(max(max(case))): # 각 영역 중 최대 높이 영역 기준 --> 그것보다 높으면 모두 잠긴 상태니깐
    check = [[False]*n for _ in range(n)] #미방문은 false로 설정
    count = 0
    for i in range(n): #주어진 수 n만큼 순회(행, 열의 수) --> i(행)뽑기
        for j in range(n): #주어진 수 n만큼 순회 --> j(열)뽑기
            if not check[i][j] and case[i][j] > k: # 미방문 + 안잠긴 상태
                dfs(i, j, k)
                count += 1
    max_count = max(max_count, count) #최대 개수 찾기
print(max_count)