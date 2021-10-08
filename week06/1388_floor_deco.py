import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# list = [input().rstrip() for _ in range(N)]

n, m = map(int, input().split())
li = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    j = 0
    while j < m:
        if li[i][j] == '|':
            j += 1
        else: # while j < m and li[i][j] == '-': 같은 의미 아닌가..
            cnt += 1
            while j < m and li[i][j] == '-':
                j += 1
for j in range(m):
    i = 0
    while i < n:
        if li[i][j] == '-':
            i += 1
        else:
            cnt += 1
            while i < n and li[i][j] == '|':
                i += 1
print(cnt)

# 리스트
# floor = []
# for _ in range(N):
#     floor.append(list(map(sys.stdin.readline().strip().split())))

# #방향 설정
# dx = [0, -1, 0, 1] # 가로
# dy = [-1, 0, 1, 0] # 세로

# def count_board(x, y):
#     count = 0
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
        
#         # 범위 내 있고, 해당 좌표 값이 0인 경우
#         if 0 <= new_x < N and 0 <= new_y < M and floor[new_x][new_y] == 0:
#             count += 1
#     return (x, y, count)

# ## 이어진 빙산이 2개 이상이거나, 총 빙산 개수가 0개면 종료
# while count < 2 and glacier_count > 0:
#     glacier_count = 0
#     count = 0
#     checker = [[0] * M for _ in range(N)] # 방문 리스트 초기값 0으로 설정

# ## bfs, dfs 모두 사용 가능/ 이어진 땅 덩어리를 탐색
#     for p in range(N): #행
#         for q in range(M): #열
#             if checker[p][q] == 0 and glacier[p][q] > 0:
#                 # 미방문 상태이고, 빙산 개수가 0보다 큰 경우
#                 glacier_count += 1 # 빙산 개수 1 추가
#                 dfs(p, q) # 이어진 빙산 찾기 
#                 count += 1 # 이어진 빙산 덩어리 개수 1 추가

# ## 이어진 빙산 덩어리가 두개 이상이면 종료
#     if count > 1:
#         break

# ## 각 지점의 melting 되는 양을 담아두고, 한번에 처리.
#     for i in range(N): #행
#         for j in range(M): #열
#             if glacier[i][j] != 0: #빙산 개수가 0이 아닌 경우
#                 melting_list.append(count_water(i, j))
#     while melting_list:
#         x, y, melt = melting_list.pop() 
#         # python에서 list는 스택의 역할을 하니깐, pop을 통해 끝에서 부터 하나씩 추출
#         glacier[x][y] -= melt #해당 빙산 높이 - 주변 물의 개수
#         if glacier[x][y] < 0: # 빙산 높이가 음수일 경우
#             glacier[x][y] = 0
#     year += 1

# if count < 2: 
#     print(0)
# else: # count > 1
#     print(year)

def 바닥장식():
    import sys

    # 입력
    N, M = map(int, sys.stdin.readline().split())
    field = [None] * N
    for i in range(N):
        field[i] = list(sys.stdin.readline().strip())

    # '-' 타일 탐색하는 함수
    def _dfs_right(x, y):
        # ''으로 마킹
        field[x][y] = ''

        # 오른쪽으로 탐색
        if y+1 < M and field[x][y+1] == '-':
            _dfs_right(x, y+1)

    # '|'타일 탐색하는 함수
    def _dfs_down(x, y):
        # ''으로 마킹
        field[x][y] = ''

        # 아래로 탐색
        if x+1 < N and field[x+1][y] == '|':
            _dfs_down(x+1, y)

    # 전체 타일 탐색
    cnt = 0                  # 타일 개수
    for i in range(N):
        for j in range(M):
            # 탐색 완료된 타일 건너뛰기
            if field[i][j] =='':
                continue
            # '-' 타일 발견 --> 오른쪽 탐색
            if field[i][j] == '-':
                _dfs_right(i, j)
            # '|' 타일 발견 --> 아래쪽 탐색
            else:
                _dfs_down(i, j)
            # 타일 개수 갱신
            cnt += 1

    # 결과 출력
    print(cnt)

바닥장식() 