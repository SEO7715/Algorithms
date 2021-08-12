import sys

N = int(sys.stdin.readline())

count = 0

for i in range(1, N+1):
    N = list(map(int, str(i)))    
    if i < 100 :
        count += 1
    elif (N[1]-N[0] == N[2]-N[1]):
        count += 1

print(count)
