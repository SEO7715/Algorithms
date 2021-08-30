import sys
input = sys.stdin.readline

multap_number, use_number = map(int, input().strip().split())
need_list = list(map(int, input().strip().split()))

named_list = [] # 콘센트에 꽂힌 리스트
answer = 0

for i in range(use_number):
     # 콘센트에 꽂을 수 있는 경우
        if need_list[i] in named_list:
            continue

        if len(named_list) < multap_number:
            named_list.append(need_list[i])
            checkIdx = i

        else: 
    
            check_index = 0
            prev = -1

            for case in named_list:
                count = 0
                for k in range(i+1, use_number): # 다시하기
                    if need_list[k] == case:
                        break
                    count += 1

                if count > prev:
                    prev = count
                    check_index = named_list.index(case)

            answer += 1           
            named_list[check_index] = need_list[i]

print(answer)
