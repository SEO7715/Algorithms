import sys
input = sys.stdin.readline

N = int(input())
fibonacci_list = [i for i in range(N+1)]

for i in range(2, N+1) :
    fibonacci_list[i] = fibonacci_list[i-1] + fibonacci_list[i-2]

print(fibonacci_list[-1]) # N 값 출력