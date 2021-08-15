import sys

n = int(sys.stdin.readline())
case_list = list(map(int, input().split()))
lis = [0] # 등차수열 대입할 리스트 만들어주기

for case in case_list: 
    if lis[-1] < case: # 주어진 케이스 보다 작으면 lis에 추가해주기
        lis.append(case) 
    else:
        left = 0
        right = len(lis)

        while left < right: 
            mid = (right + left)//2 
            if lis[mid] < case:
                left = mid + 1
            else:
                right = mid #왜..?
        lis[right] = case

print(len(lis)-1) #처음에 넣어준 lis = [0] 에서 0 은 카운트 제외해주어야 하니깐!