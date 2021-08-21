import sys
input = sys.stdin.readline

R, C = tuple(map(int, input().split())) 
matrix = []
START, GOAL = None, None
WIZARD = [] #물

for r in range(R):
    row = [v for v in input().rstrip()]
    # print(row) ['D', '.', '*']
    for c, value in enumerate(row):
        if value == "D":
            GOAL = (r, c)
            # print(GOAL)
        elif value == "S":
            START =(r, c)
            # print(START) (2, 1)
        elif value == "*":
            WIZARD.append((r, c))
            # print(WIZARD) [(0, 2)]
    matrix.append(row)

# 방향 설정
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# frontier 큐 생성 : 행위자 정보를 함께 저장/ 홍수 먼저, 고슴도치 다음
frontier = [(v, "*") for v in WIZARD] + [(START, "S")]
# print(frontier) [((0, 2), '*'), ((2, 1), 'S')]

time = 0
success = False

while not success and frontier: # success가 false이고, froniter가 있는 동안
    time += 1 
    next_frontier = [] # 다음 방문할..frontier..?
    for v1, actor in frontier: #actor가 무슨역할..? v1이 물/ actor가 고슴도치 인가..?
        x1, y1 = v1
        for dx, dy in zip(dxs, dys):
            x2, y2 = x1+dx, y1+dy
            v2 = (x2, y2) #새로운 x, y
            # 존재하는 위치인지 확인
            if x2 < 0 or x2 >= R or y2 < 0 or y2 >= C:
                continue
            # 장애물이 놓인 위치인지 확인
            status = matrix[x2][y2]
            if status == "X":
                continue
            if actor == "*" and (status in [".", "S"]):
                matrix[x2][y2] = "*"
                next_frontier.append((v2, "*"))
            elif actor == "S" and status == "D":
                matrix[x2][y2] = "S"
                success = True
                break
            elif actor == "S" and status == ".":
                matrix[x2][y2] = "S"
                next_frontier.append((v2, "S"))
    frontier = next_frontier 

if success: 
    print(time) 
else:
    print("KAKTUS")  

