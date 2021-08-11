import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline()) #행과 열의 개수
# maps = [] #위치별 점수 리스트
maps = [list(map(int, input().split())) for _ in range(n)]

# for x in range(n): 
#     zxc = []
#     for p in map(int, sys.stdin.readline().split()):
#         zxc.append(p)
#     maps.append(zxc)

dx = [-1, 0, 1, 0] # 1이면 위로 한칸, -1이면 아래로 한칸 #행방향
dy = [0, -1, 0, 1] # 1이면 오른쪽으로 한칸, -1이면 왼쪽으로 한칸 #열방향
max_count = 1 # 가능한 최솟값으로 설정
visited = [[False] * n for _ in range(n)] #미방문은 false로 설정

def dfs(level, x, y): # 높이, 행, 열
    global n, maps, visited, dx, dy
    for i in range(4): # 4범위 순회(0, 1, 2, 3)
        nx = x + dx[i] # dx[0] = -1/ dx[1] = 0/ dx[2] = 1/  dx[3] = 0
        ny = y + dy[i] # dy[0] = 0/ dy[1] = -1/ dy[2] = 0/  dy[3] = 1

        if 0 <= nx < n and 0 <= ny < n: # nx, ny가 n보다 작으면 (ex.행, 열이 5를 넘어갈 수 없으니깐)
            if level < maps[nx][ny] and not visited[nx][ny]: # maps[nx][ny]의 값(해당 위치의 높이)이 기준 높이보다 높고, 미방문 상태라면([False] 이면)
                visited[x][y] = True #방문 리스트에 넣어준 값을 True로 해주기

# for level 문 순회하면서 각 level에대한 안전지역의 개수 추출 --> 개수들 중 최대값
for level in range(1, 101): #높이는 1이상 100이하의 정수
    count = 0
    for i in range(n): #주어진 수 n만큼 순회(행, 열의 수) --> i(행)뽑기
        for j in range(n): #주어진 수 n만큼 순회 --> j(열)뽑기
            if maps[i][j] > level and not visited[i][j]: # maps[i]][j]의 값(해당 위치의 높이)이 기준 높이보다 높고, 미방문 상태라면([False] 이면)
                visited[i][j] = True #방문 리스트에 넣어주기
                dfs(level, i, j) #dfs 함수에 대입하여 실행
                count += 1 #다음 호출을 위해
    if max_count < count: 
        max_count = count

    # if count == 0:
    #     break
    # max_count = max(max_count, count)
    print(max_count)

# 1. 모든 점을 시작점으로 탐색을 시작
# 2-1. 해당 지점이 방문했던 점이라면 다음 지점으로 넘어감
# 2-2. 처음 방문하는 지점이면, 좌,우,상,하 탐색을 이어가기
# 3. 남은 점이 없다면 탐색을 종료
# 4. 1~2과정에서, 안전지역의 개수를 확인


