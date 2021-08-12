import sys
from itertools import permutations # tuple로 경우의 수가 나옴 --> list화

# 20 1 15 8 4 10 
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers_case = list(permutations(numbers, N)) # n개 만큼 배열할 수 있는 리스트 경우의 수
inner_list = []

max_sum = 0

for i in range(len(numbers_case)):
    inner_list = numbers_case[i]
    differ_list = []
    for j in range(len(inner_list)-1):
        # sum_differ = 0
        sum_differ = abs(inner_list[j] - inner_list[j+1])
        differ_list.append(sum_differ)
        # print(sum(differ_list))
    max_sum = max(max_sum, sum(differ_list))
print(max_sum)


            
            #differ_list 에는 각 innerlist에 대한 differ값이 저장되어야 함
            # inner_list를 갱신할때마다 differ_list=[]로 초기화 필요
            # sum_differ.append(sum(differ_list))
            # differ_list = []
            #'int' object has no attribute 'append'
# max_sum = max(max_sum, sum_differ)
# print(max_sum)

