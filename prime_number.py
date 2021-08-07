import sys

N = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().split()))

print(C)

# (C[i] % 3 == 0) or (C[i] % 5 == 0) or (C[i] % 7 == 0):

for i in range(len(C)):
    if (C[i] % i == 0):
        del C[i]
    else :
        print(C[i])

# 에라토스테네스 체
# 3, 5, 7, 9...n : 지우게 되는 첫번째 = 소수 2
# 5, 7, .... : 3


