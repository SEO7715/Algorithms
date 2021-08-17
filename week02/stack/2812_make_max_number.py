import sys

N, K = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline())

k = K
stack = []

for i in range(N): 
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])

print(''.join(stack[:N-K]))
