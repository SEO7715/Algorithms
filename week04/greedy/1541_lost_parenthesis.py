import sys
input = sys.stdin.readline

calculation_list = input().strip().split('-')
sum = 0

for first_number in calculation_list[0].split('+'):
    sum += int(first_number)

for second_number in calculation_list[1:]:
    for last_number in second_number.split('+'):
        sum -= int(last_number)

print(sum)
