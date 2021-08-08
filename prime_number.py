import sys

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
prime_number = 0


for n in number_list:
    count = 0
    if n == 1:
        count += 1
    elif n == 2:  
        prime_number += 1 
    elif n > 2:
        for i in range(2, n): #  2부터 n-1까지 --> n까지 포함하면, 자기자신을 나누니깐
        # for i in range(2, int(n**0.5)+1): #에라토스테네스 체 적용 --> 루트 n으로 나눌 수 있으면, 거기까지만 확인하면 됨 
        # (루트n 뒤로 나오는 숫자는 앞에 나온 수에 대한 쌍)
            if (n % i == 0): 
                count += 1
                break
        if count == 0:
            prime_number += 1

print(prime_number)



# 에라토스테네스 체
# 3, 5, 7, 9...n : 지우게 되는 첫번째 = 소수 2
# 5, 7, .... : 3