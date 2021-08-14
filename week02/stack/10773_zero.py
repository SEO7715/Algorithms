import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    value  = int(sys.stdin.readline())

    if value == 0: 
        stack.pop()
    else:
        stack.append(value)
    
print(sum(stack))