import sys
 
input = sys.stdin.readline
n = int(input())
number_list = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n):
    number = number_list[i] 
    while stack and number_list[stack[-1]] < number:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)
    
# print(' '.join(map(str, result)))