import sys

T = int(sys.stdin.readline())

for _ in range(T):
    case  = sys.stdin.readline()
    case_list = list(case)
    sum = 0

    for j in case_list:
        if j == "(": 
            sum += 1

        elif j == ")":
            sum -= 1
        
        if sum < 0: #왜이렇게해야하지..? 반대로 하면 에러남,,왜지..?
            print("NO")
            break

    if sum == 0:
        print("YES")
    
    elif sum > 0: #왜이렇게해야하지..? 반대로 하면 에러남,,왜지..?
        print("NO")
        
    