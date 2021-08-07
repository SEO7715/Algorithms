pos = [0] * 8 # 각 열에서 퀸의 위치
flag = [False] * 8 # 각 행에 퀸을 배치했는지 체크

def put(): # 위치설정 (n개를 배치하는 방법을 정할 때마다 실행)
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int): #실제 배치
    for j in range(8):
        if not flag[j]: # flag[j] = [False] 이면, 
            pos[i] = j # i번째 열에, j번째 행에 퀸 배치
            if j == 7: # 모두 배치를 완료했으면,
                put()   # 출력해라 (A번째 열에, 0,1,2,3 모두 확인)
            else:
                flag[j] = True #j번째 행에는 배치를 했으니깐,
# 다른 경우의 수를 확인할 때는 true여야 하므로 false를 true로 바꿔줌
                set(i + 1)  #set(0)에서 set(1)을 호출하고
                flag[j] = False #set(1)이 끝난 다음에, flag(j)를 false로 바꿔줌 (put()실행 후)

set(0)
