import sys
 
input = sys.stdin.readline
n = int(input())
tower_list = list(map(int, input().split()))
stack = []
result = [0] * n # 0으로 기본값 설정해주기

for i in range(n): 
    tower = tower_list[i] 
    while stack and tower_list[stack[-1]] < tower: # 스택이 있고, tower_list의 stack의 가장 최근 값이 tower_list[i]보다 작으면
        stack.pop() # stack 가장 최근 값 날리기
    if stack: # 스택이 있고, tower_list의 stack의 가장 최근 값이 tower_list[i]보다 크면
        result[i] = stack[-1] + 1 # 스택의 인덱스 값에 1 더해주기(인덱스는 0부터 세니깐)
    stack.append(i) # stack에 i값 추가
print(' '.join(map(str, result))) # [0, 0, 2, 2, 4] --> 0 0 2 2 4로 출력