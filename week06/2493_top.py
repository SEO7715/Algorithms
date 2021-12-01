import sys
input = sys.stdin.readline

top_N = int(input())
top_list = list(map(int, input().split()))

stack = [] 
answer = [0] * top_N

for i in range(top_N):
    top = top_list[i]
    while stack and stack[-1] < top:
        stack.pop()
    if stack and stack[-1] > top:
        answer[i] = stack[-1] + 1 # indexError // 그럼 여기서 인덱스 번호를 어떻게 넣어주나,,?
    stack.append(top)
    
print(answer)
