def move(no: int, x: int, y: int):
    if no > 1:
        move(no -1, x, 6-x-y)
    print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다.')

    # if no > 1:
    #     move(no -1, 6-x-y, y)
