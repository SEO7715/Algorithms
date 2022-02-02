import math
import sys

input = sys.stdin.readline
number_list, differ_list = [], []
differ_num = 0
count = 0
# differ_list = [2, 4, 7, 8]

N = int(input())
for _ in range(N):
    number_list.append(int(input()))

# 숫자들 간의 간격(차) differ_list에 넣기
for i in range(1, N):
    differ_list.append(number_list[i] - number_list[i-1])

# 최대공약수 구하기
for j in range(len(differ_list)):
    differ_num = math.gcd(differ_list[j], differ_num)

print(differ_num)
# 최대공약수만큼 더해주기(number_list의 마지막 숫자까지)
result = ((number_list[-1] - number_list[0]) // differ_num) + 1 - N

print(result)