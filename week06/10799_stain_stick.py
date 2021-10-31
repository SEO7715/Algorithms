import sys
input = sys.stdin.readline

string = input().strip()

stack = []
lazer_cnt = 0
stick_cnt = 0
before = ""

for char in string:
    # "("
    if char == "(":
        stack.append(char)
        before = char
        continue
    stack.pop()
    # ")"
    if before == "(": #레이저
        lazer_cnt += len(stack)
    else: # 막대기
        stick_cnt += 1

    before = char

print(lazer_cnt + stick_cnt)

