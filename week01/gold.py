import sys

def prime_number(number): #소수 찾기 함수
    if  number < 2:
        return False #return은 함수 내에서만 사용 가능
    
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            return False
    return True #for문이 끝나고 실행("True"문자열보다 True boolean이 더 속도 빠름)
    # not "True" 와 False는 다름 "True"와 "False"는 True임

T = int(sys.stdin.readline())

for j in range(T):
    n = int(sys.stdin.readline())
    half_n = int(n//2)

    for a in range(half_n, 1, -1):
        if prime_number(a) == True and prime_number(n-a) == True:
            print(a, n-a)
            break


