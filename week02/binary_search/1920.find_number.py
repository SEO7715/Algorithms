
import sys

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split())) 

M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split())) 


for i in range(M):
    if check_list[i] in number_list:
        print(1)
    else:
        print(0)

