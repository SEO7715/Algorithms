import sys

n = int(sys.stdin.readline())

points = []
for _ in range(n):
    c, r = list(map(int, sys.stdin.readline().split()))
    points.append(("L", c-r))
    points.append(("R", c+r))

points.sort(key=lambda p: (-p[1], p[0]), reverse=True) # 좌표 기준 오름차순 정렬(오 > 왼 순서, 문자열 역순 정렬)

stack = [] #스택 생성
area = 1 # 영역 개수 1로 설정

for curr in points:
    if curr[0] == "L":
        stack.append(curr)
        continue # for문 재실행

    # 오른쪽 끝인 경우
    cum_width = 0
    while stack:
        prev = stack.pop()
        if prev[0] == "C": 
            cum_width += prev[1]
        elif prev[0] == "L":
            width = curr[1] - prev[1] # 지름길이를 구하면, 너비 값을 알 수 있음
            if width == cum_width: # 상위원 너비 = 하위원들의 너비 합 일치할 경우
                area += 2 
            else:
                area += 1
            stack.append(("C", width))
            break

print(area) 
            

