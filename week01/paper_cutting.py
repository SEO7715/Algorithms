import sys

x, y = map(int, sys.stdin.readline().split())
x_list = [0, y]
y_list = [0, x]
x_length = []
y_length = []

c = int(sys.stdin.readline())

for i in range(c):
    s = list(map(int, sys.stdin.readline().split()))
    if (s[0] == 0):
        x_list.append(s[1])
    else :
        y_list.append(s[1])

x_list.sort()
y_list.sort()

for i in range(1, len(x_list)): #list[1] 부터
    x_length.append(x_list[i] - x_list[i-1])

for i in range(1, len(y_list)):
    y_length.append(y_list[i] - y_list[i-1])

print(max(x_length) * max(y_length))
