#단순삽입정렬
import sys

N = int(sys.stdin.readline())

number_list = []

for i in range(N):
    number_list.append(int(sys.stdin.readline()))

for i in range(1, len(number_list)):
    while (i > 0 and (number_list[i] < number_list[i-1])):
        number_list[i], number_list[i-1] = number_list[i-1], number_list[i]

        i -= 1
for j in number_list:
    print(j)

#버블정렬
# import sys

# N = int(sys.stdin.readline())

# number_list = []

# for i in range(N):
#     number_list.append(int(sys.stdin.readline()))

# for i in range(len(number_list)-1):
#     exchange = 0
#     for j in range(len(number_list)-1, i, -1):
#         if number_list[j-1] > number_list[j]: #i가 더 큰 값이어야 함
#             number_list[j-1], number_list[j] = number_list[j], number_list[j-1]
#             exchange += 1
#     if exchange == 0:
#         break

# for j in number_list:
#     print(j)

# Sorted() 함수 사용 --> 속도 빠름
# import sys

# N = int(sys.stdin.readline())

# number_list = [None] * N 

# for i in range(N):
#     number_list[i] = int(sys.stdin.readline())

# number_list = sorted(number_list)

# for i in range(N):
#     print(number_list[i])