import sys
input = sys.stdin.readline

array = input()
stack = []

for i in range(len(array)):
    count = 0
    if array[i] == '(': 
        stack.append(array[i])
    else: # ')'일 경우
        if stack and stack[-1] == '(': #레이저일 경우
            count += 1
            stack.pop()

    print(count)
    
