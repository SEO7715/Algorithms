import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001

for i in range(N):
    num_list[int(sys.stdin.readline())] += 1


num_list = sorted(set(num_list))

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

