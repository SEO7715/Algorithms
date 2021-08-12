import sys

n = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_number():
    for i in  range(len(number_list)):
        if number_list[i] in case:
            if i == 1:
                number_list[i] = 1
            if i == 2:
                number_list[i] = 2
            if i == 3:
                number_list[i] = 4
            if i > 3:
                number_list[i] = number_list[i-1] + number_list[i-2] + number_list[i-3]

# print(find_number())

print(find_number(5))

# print(number_list[]) --> 

# for i in range(len(case)):
#     if i in number_list:
#         find_number(i)







