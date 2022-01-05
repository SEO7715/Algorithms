a = 5
b = 3

def solution(a, b):
    result = 0
    if a > b:
        a, b = b, a 
    for number in range(a, b+1):
        result += number
    return result

print(solution(a, b))