import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(input()))


num = sorted(set(num))

for i in num:
    print(i)