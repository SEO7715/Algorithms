# 2577번 (숫자의 개수)

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = list(str(a * b * c))

for i in range(10): #0부터 9까지
    print(result.count(str(i))) # 0~9 중 하나인 i값을 문자열로 변환해서, 일치하는 것 count 