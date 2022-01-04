dartResult = '1D2S#10S'

def solution(dartResult):
    stack = []
    bonus = { 'S':1, 'D':2, 'T':3 }
    dartResult = dartResult.replace('10', 'A')
    for char in dartResult:
        if char.isdigit():
            stack.append(int(char))
        elif char == 'A':
            stack.append(10)
        elif char in bonus:
            stack.append(stack.pop() ** bonus[char])
        elif char == '*':
            number = stack.pop() * 2
            if stack:
                stack.append(stack.pop() * 2)
            stack.append(number)
        elif char == '#':
            stack.append(stack.pop() * (-1))
    return sum(stack)

print(solution(dartResult))