import sys
input = sys.stdin.readline
def nCr(n, r):
    result = 1
    if r > n-r:
        r = n-r
    for i in range(n, n-r, -1):
        result *= i
    for j in range(1, r+1):
        result //= j
    return result

result_list = []
N = int(input())

for _ in range(N):
    west, east = map(int, input().split())
    result_list.append(nCr(east, west))


print(*result_list, sep='\n')
