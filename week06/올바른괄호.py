
s = "(())()"	

def solution(s):
    answer = True
    stack = []
    for case in s:
        if case == "(":
            stack.append(case)
        else: # ")"인 경우
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(case)
    if len(stack) != 0:
        answer = False
    return answer

print(solution(s))
