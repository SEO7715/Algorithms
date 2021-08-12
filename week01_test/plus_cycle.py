import sys

number = int(sys.stdin.readline())
check_number = number

count = 0
while True:
    sum_number = (number // 10) + (number % 10)
    new_number = (10 * (number % 10)) + (sum_number % 10)
    count += 1
    if new_number == check_number:
        break
    number = new_number
        
print(count)
    