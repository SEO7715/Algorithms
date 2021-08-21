import sys
from collections import deque
input = sys.stdin.readline

M, N, H = tuple(map(int, input().split())) 

matrix = [] # 매트릭스 구성
frontier = [] 
# 여러개 익어 있는 토마토를 시작점의 frontier로 판단
# --> 기존에 익어 있는 토마토를 visit 내역의 시작시점으로 본다는 의미
goal_count = 0 # 익어야 하는 개수

for h in range(H):
    space = []
    for x in range(N):
        row = list(map(int, input().split()))
        space.append(row)
        # print(space) [[0, -1, 0, 0, 0], [-1, -1, 0, 1, 1], [0, 0, 0, 1, 1]]
        for y in range(M):
            if row[y] == 1: #익은 토마토
                frontier.append((h, x, y))
                # print(frontier)
                # [(0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4)] 
            elif row[y] == 0: #익지 않은 토마토
                goal_count += 1
    matrix.append(space)
    # print(matrix) [[[0, -1, 0, 0, 0], [-1, -1, 0, 1, 1], [0, 0, 0, 1, 1]]]
    # space 에 row 내역 넣어주고,, matrix에 space 넣어주기 --> 이케 3차원 만드는  

def bfs(matrix, frontier):
    # 탐색하기
    # 매트리스 값이 0일 경우, 미방문 상태
    # 매트릭스 값이 1이상일 경우, 방문된 상태이며 해당 숫자는 방문 순번을 의미
    search_count = 0 # 탐색한 위치 수 초기 값 설정
    if goal_count == 0: # 탐색할 위치가 없다면, 종료
        return search_count 

    max_time = 0 # 탐색 소요 시간 초기 값 설정

    # 방향 설정
    dhs = [0, 0, 0, 0, -1, 1]
    dxs = [-1, 1, 0, 0, 0, 0]
    dys = [0, 0, -1, 1, 0, 0]

    frontier = deque(frontier)

    while frontier:
        v1 = frontier.popleft() #(0, 1, 3)
        v1_h, v1_x, v1_y = v1
        v1_time = matrix[v1_h][v1_x][v1_y] 

        for dh, dx, dy in zip(dhs, dxs, dys): #zip -> 순회가능한 이터레이터 객체 사용 위해 
            h = v1_h + dh
            x = v1_x + dx
            y = v1_y + dy
            
            # 매트릭스 상 존재 여부 확인
            if h < 0 or h >= H or x < 0 or x >= N or y < 0 or y >= M:
                continue

            if matrix[h][x][y] != 0: #값이 -1 또는 1인 경우 방문 불필요
                continue
            search_count += 1 # 새로운 위치인 경우
            matrix[h][x][y] = v1_time + 1 # 새로운 위치의 시간 표시
            if max_time < v1_time:
                max_time = v1_time #max_time 값 업데이트

            frontier.append((h, x, y)) #해당 h, x, y 값 큐에 넣기
        
    if search_count == goal_count: #익어야 하는 개수와 탐색한 개수가 일치할 경우
        return max_time #최소 소요시간 출력
    else:
        return -1 # 모두 익지 못하는 상황일 경우 -1 출력

print(bfs(matrix, frontier))
