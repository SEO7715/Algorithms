import sys
from itertools import permutations

# 20 1 15 8 4 10 
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split())) 

maximum = 0

for case in set(permutations(array, N)):
    total = 0
    for i in range(len(case)-1):
        total += abs(case[i] - case[i+1])

    maximum = max(maximum, total)

print(maximum)