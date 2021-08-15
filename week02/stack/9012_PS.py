import sys

T = int(sys.stdin.readline())
stack= []

for _ in range(T):
    ps = sys.stdin.readline()
    is_empty = False
    for i in range(len(ps)):
        if ps[i] == "(": 
            stack.append(ps[i])
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty: #스택이 없고, 데이터가 비어 있는 게 아니면
        print("YES")
    else:
        print("NO")