import collections
import sys

N = int(sys.stdin.readline().strip())
apple = int(sys.stdin.readline().strip())

apple_location = []
for _ in range(apple):
    apple_x, apple_y = map(int, sys.stdin.readline().strip().split())
    apple_location.append((apple_x, apple_y))

L = int(sys.stdin.readline().strip())

movement = collections.deque()
for _ in range(L):
    #movetime도 str다!!
    move_time, move_direct =sys.stdin.readline().strip().split()
    movement.append((move_time, move_direct))

## 오 아 왼 위           ## 오른쪽 꺽으면 index +1,  왼쪽 꺾ㄱ으면 index - 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

snake_location = collections.deque()
snake_location.appendleft((1, 1))
moving_way = 0

## 방향을 전환해주는 함수
def snake_move(way):
    global moving_way
    if way == 'L':
        moving_way -= 1
    else:
        moving_way += 1
## moving_way = (moving_way - 1) % 4 보다 아래가 더 빠르다! 나누기 연산이 오래 걸리는 듯.
    if moving_way < -4:
        moving_way += 4
    elif moving_way > 3:
        moving_way -= 4

time = 0

while 0 < snake_location[0][0] <= N and 0 < snake_location[0][1] <= N:
    time += 1
    now_head = snake_location[0]
    snake_location.appendleft((now_head[0] + dy[moving_way], now_head[1] + dx[moving_way])) #이해못함..
    # appendleft()는 왼쪽에 값을 입력하고자 할 때 사용 

    temp_head = snake_location.popleft()
    if temp_head in snake_location:
        break
    snake_location.appendleft(temp_head)

    if snake_location[0] not in apple_location:
        snake_location.pop()
    else:
        apple_location.remove(snake_location[0])

    if movement and int(movement[0][0]) == time:
        snake_move(movement.popleft()[1])

print(time)









### 뱀의 머리부터 꼬리까지의 좌표를 deque로 표현, 1초 가면 꼬리 자르고 머리 추가하고
### 뱀의 머리가 정사각형 사이일 때까지 while문. 부딪히면 while문이 끝나는 식으로
### + 뱀의 몸과 부딪힐 수도 있음