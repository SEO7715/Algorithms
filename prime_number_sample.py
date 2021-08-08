import sys

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
prime_number = 0

for number in number_list:
    count = 0
    if number == 1:
        count += 1
    elif number > 1:
        for i in range(2, number):
            if (number % i == 0):
                count += 1
                break
        if count == 0:
            prime_number += 1

print(prime_number)


