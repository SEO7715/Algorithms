import sys
input = sys.stdin.readline

R, C = tuple(map(int, input().split()))
matrix = []
START, GOAL = None, None
WIZARD = [] #물

for r in range(R):
    row = [v for v in input().rstrip()]
    for c, value in enumerate(row):
        # print(c) 인덱스 번호
        # print(value) 인덱스 값
        if value == "D":
            GOAL = (r, c)
            # print(GOAL) 비버굴 위치
        elif value == "S":
            START = (r, c)
            # print(START) 시작점 위치
        elif value == "*":
            WIZARD.append((r, c))
            # print(WIZARD) 물 위치
    matrix.append(row)

# 방향 설정
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# frontier 큐 생성: 행위자 정보를 함께 저장/ 물 -> 고슴도치 순서
frontier = [(v, "*") for v in WIZARD] + [(START, "S")]

time = 0
success = False

while not success and frontier:
    time += 1
    next_frontier = []
    for v1, actor in frontier:
        x1, y1 = v1
        for dx, dy in zip(dxs, dys):
            x2, y2 = x1 + dx, y1 + dy
            v2 = (x2, y2)
            if x2 < 0 or x2 >= R or y2< 0 or y2 >= C:
                continue
            status = matrix[x2][y2]
            if status == "X":
                continue
            if actor == "*" and (status in [".", "S"]): 
                # 행위자가 *이고, 현재 매트릭스 위치가 [".", "S"] 에 있으면
                matrix[x2][y2] = "*" # matrix[x2][y2]는 * 값이 된다
                next_frontier.append((v2, "*")) # next_frontier에 v2, "*" 추가해주기
            elif actor == "S" and status == "D": # 행위자가 S이고, 현재 매트릭스 위치가 D이면 
                matrix[x2][y2] = "S" # 매트릭스 위치 값은 S이고
                success = True #도착 성공
                break
            elif actor == "S" and status == ".":
                matrix[x2][y2] = "S"
                next_frontier.append((v2, "S"))
    frontier = next_frontier

if success:
    print(time)
else:
    print("KAKTUS")
                
