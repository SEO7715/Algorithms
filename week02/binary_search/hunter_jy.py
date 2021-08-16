import sys

shooting_spot, animal_num, shooting_range = map(int, sys.stdin.readline().strip().split())
x_arr = list(map(int, sys.stdin.readline().strip().split()))
animals_spot = [list(map(int, sys.stdin.readline().strip().split()))for _ in range(animal_num)]

# y좌표를 비교해서 되는지 안되는지 확인. (사정거리랑 비교)
# x좌표가 좌, 우측 어느 쪽에 있는지 확인 후 이분 탐색 때리기
hunting_count = 0
x_arr.sort()

def cal_distance(shooting_x, x, y):
    return abs(shooting_x - x) + y    

for animal in animals_spot:
    animal_x = animal[0]
    animal_y = animal[1]

    if animal_y > shooting_range:
        continue 

    pl = 0
    pr = shooting_spot - 1

    while pl <= pr:
        pc = (pl + pr) // 2

        if cal_distance(x_arr[pc], animal_x, animal_y) <= shooting_range:
            hunting_count += 1
            break
        else:
            if animal_x < x_arr[pc]:
                pr = pc - 1
            else:
                pl = pc + 1

print(hunting_count)
