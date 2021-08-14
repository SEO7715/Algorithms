import sys

N = int(sys.stdin.readline())

stick_list = []
count = 1

for _ in range(N):
    stick_list.append(int(sys.stdin.readline()))

x = stick_list[-1]

for i in range(len(stick_list)-1, -1, -1):
    if stick_list[i] > x :
        count += 1
        x = stick_list[i]
print(count)