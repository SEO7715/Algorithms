import sys
import collections
sys.setrecursionlimit(10000)

# N 행 / M 열 
N, M  = map(int, sys.stdin.readline().strip().split()) 

# 빙산 리스트
glacier = []
for _ in range(N):
    glacier.append(list(map(int, sys.stdin.readline().strip().split())))

#방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

## 주변에 물이 몇개인지 세주는 함수
def count_water(x, y):
    count = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        # 범위 내 있고, 해당 좌표 값이 0인 경우
        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] == 0:
            count += 1
    return (x, y, count)

## dfs를 이용하여, 이어진 빙산 탐색
def dfs(x, y):
    checker[x][y] = 1 # 방문 표시
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        # 범위 내 있고, 해당 좌표 값이 양수인 경우,  
        if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] > 0:
            if checker[new_x][new_y] == 0: # 미방문 상태이면
                checker[new_x][new_y] = 1 # 방문 상태로 바꿔주기
                dfs(new_x, new_y)

# ## bfs를 이용하여, 이어진 land를 탐색
# queue = collections.deque()
# def bfs(x, y):
#     queue.append((x, y))
#     checker[x][y] = 1 # 방문표시
#     while queue:
#         p, q = queue.popleft()

#         for i in range(4):
#             new_x = p + dx[i]
#             new_y = q + dy[i]

#             if 0 <= new_x < N and 0 <= new_y < M and glacier[new_x][new_y] > 0:
#                 if checker[new_x][new_y] == 0:
#                     checker[new_x][new_y] = 1
#                     queue.append((new_x, new_y))

glacier_count = 1 # 빙산 개수 (while 조건 glacier_count > 0이므로 1로 설정해줌)
count = 0 # 이어진 빙산 덩어리 개수
year = 0 # 연도

melting_list = []

## 이어진 빙산이 2개 이상이거나, 총 빙산 개수가 0개면 종료
while count < 2 and glacier_count > 0:
    glacier_count = 0
    count = 0
    checker = [[0] * M for _ in range(N)] # 방문 리스트 초기값 0으로 설정

## bfs, dfs 모두 사용 가능/ 이어진 땅 덩어리를 탐색
    for p in range(N): #행
        for q in range(M): #열
            if checker[p][q] == 0 and glacier[p][q] > 0:
                # 미방문 상태이고, 빙산 개수가 0보다 큰 경우
                glacier_count += 1 # 빙산 개수 1 추가
                dfs(p, q) # 이어진 빙산 찾기 
                count += 1 # 이어진 빙산 덩어리 개수 1 추가

## 이어진 빙산 덩어리가 두개 이상이면 종료
    if count > 1:
        break

## 각 지점의 melting 되는 양을 담아두고, 한번에 처리.
    for i in range(N): #행
        for j in range(M): #열
            if glacier[i][j] != 0: #빙산 개수가 0이 아닌 경우
                melting_list.append(count_water(i, j))
    while melting_list:
        x, y, melt = melting_list.pop() 
        # python에서 list는 스택의 역할을 하니깐, pop을 통해 끝에서 부터 하나씩 추출
        glacier[x][y] -= melt #해당 빙산 높이 - 주변 물의 개수
        if glacier[x][y] < 0: # 빙산 높이가 음수일 경우
            glacier[x][y] = 0
    year += 1

if count < 2: 
    print(0)
else: # count > 1
    print(year)