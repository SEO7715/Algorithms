test_case = int(input())

for _ in range(test_case):
    ps = input()
    stack = []
    is_empty = False

    for i in range(len(ps)):
        # print(i)
        if ps[i] == "(":
            stack.append(i)
        else: 
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty:
        print("YES")
    else:
        print("NO")