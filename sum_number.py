import sys

N = int(sys.stdin.readline())
number = sys.stdin.readline()

number_list = list(number)

for i in range(len(number)):
    count = 0
    count += i
    print(count)


# sum_number = sum(number_list)
# print(number_list)
