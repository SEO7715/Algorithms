# def hanoi (원반개수(n), 시작(source), 목표(destination), 보조(auxiliary)):
#     if 원반개수(n) == 1:
#         print(시작, '->', 목표)
#         return
#     hanoi(원반개수(n)-1,  시작(source), 보조(auxiliary), 목표(destination))
#     print(시작, '->', 목표)
#     hanoi(원반개수 -1, 보조, 목표, 시작)

#  "n-1개를 a에서 b로 옮기고" 
# "남은 1개를 a에서 c로 옮기고" 
# "n-1개를 b에서 c로 옮기는"
############################################
# 첫번째 방법
import sys

N = int(sys.stdin.readline())
def hanoi(N, src, des, aux):
    if N == 1:
        print(src, des)
        return
    else:
        hanoi(N-1, src, aux, des)
        print(src, aux)
        hanoi(N-1, aux, des, src)

print(hanoi(N, 1, 3, 2))
#############################################
# 2번째 방법
def move(N, x, y):
    if N > 1:
        move(N-1, x, 6-x-y) ## 여기서 6은 하노이 기둥 1, 2, 3을 표시해주기 위한 것/
        # a,b,c 세가지 수에서 임의의 두 수를 제외한 한가지 수를 골라내기 위해서는 (A + B + C )- a - b = c

    print(str(x) + ' ' + str(y))

    if N > 1:
        move(N-1, 6-x-y, y)

N = int(input())
print(2 ** N - 1)	# 횟수
if N <= 20:
    move(N, 1, 3)
