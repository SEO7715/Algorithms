s = input()

def is_check(s): # 올바른 괄호열 여부 확인
    stack = []
    flag = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        else:  # )] 일 경우
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
        
    if not stack and flag:
        return True
    return False

def calc_value(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '(':
                            stack[-1] = temp * 2
                            print()
                            break
                        else:
                            temp += stack[-1]
                            stack.pop()
            else: # ]
                if stack[-1] == '[':
                    stack[-1] = 3
                else: 
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '[':
                            stack[-1] = temp * 3
                            break
                        else: 
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)

if is_check(s):
    print(calc_value(s))
else:
    print(0)
