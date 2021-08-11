import sys
# 2557
# print("Hello World!")

# 10869 (사칙연산)
# import sys

# a, b =map(int, sys.stdin.readline().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
#######################################################

# 2588 오답
# a, b, c, d, e, f, x, y, z, t = int(input().split())

# x = (100*a + 10*b + c)*d
# y = (100*a + 10*b + c)*e
# z = (100*a + 10*b + c)*f

# t = x + 10*y + 100*z

# print(t)

# 2588 (세자리 수 곱셈/ 곱하기)
# string이 배열로 저장됨 
# n1 = int(input()) 
# n2 = input() #string

# print(n1 * int(n2[2]))
# print(n1 * int(n2[1]))
# print(n1 * int(n2[0]))
# print(n1 * int(n2))
#######################################################

# 9498번 (점수별 등급, 시험성적)

# a = int(input()) 

# if 90 <= a <= 100 : 
#     print("A")
# elif 80 <= a <= 89 : 
#     print("B")
# elif 70 <= a <= 79 :
#     print("C")
# elif 60 <= a <= 69 : 
#     print("D") 
# else :
#     print("F")
#######################################################

# 2753번(윤년)

# a = int(input())
# if (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0) :
#     print(1)
# else :
#     print(0)
#######################################################

# 1085번 (최솟값) min()
# x, y, w, h = map(int, input().split())

# print(min([x, y, w-x, h-y]))
#######################################################

# 2739번 (구구단)
# n = int(input())

# for j in range(1, 10):
#     print(n, "*", j, "=", n*j)
#######################################################

# 10950번 (a+b)
# T = int(input())

# for i in range(T):
#     A, B = map(int, input().split())
#     print(A + B)
#######################################################

# 2438번  (별찍기)
# N = int(input())

# for i in range(1, N+1):
#     print("*" * i)
#######################################################

# 10871번 (x보다 작은 수)
# N, X = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))

# for i in range(N):
#     if A[i] < X :
#         print(A[i], end = " ")
#######################################################
#######################################################
#######################################################
#######################################################

# 2562번 (최댓값)
b = []

for i in range(9):
    a = int(sys.stdin.readline())
    b.append(a)
print(b)
max_num = max(b)
print(max_num)
print(b.index(max_num)+ 1)


# 8958번 (ox퀴즈) 다시하기

#######################################################
#######################################################

# 15596번 (정수 n개의 합--> 함수로!)
# 가우스의 덧셈으로 푸는 방법
# n = int(sys.stdin.readline())
# sum = n * (n + 1) // 2

# print(sum)

# def solve(a):
#     ans = sum(a)
#     return ans


#######################################################
#######################################################
# 4344번(평균) 다시하기
import numpy 

# C = int(sys.stdin.readline())
# count = 0

# for i in range(C):
#     score = list(map(int, sys.stdin.readline().split()))
#     average = sum(score[1:]) // score[0]
# ---> 0번째 값은 학생수니깐..! 없애줘야 함

#     for j in score[1:]:
#         if average < j:
#             count += 1
#     print("%.3f%%"%((count/score[0]))*100)
#     count = 0
    
#######################################################

# 2675번 (문자열 반복)
# T = int(sys.stdin.readline())

# for i in range(T):
#     R, S = sys.stdin.readline().split()
#     for j in S:
#         print(j*int(R), end="")


#######################################################
# 1152번 (단어의 개수)
# T = len(sys.stdin.readline().split())
# print(T)

#######################################################
# 2908번 (상수)
# import sys 

# a, b = map(str, sys.stdin.readline().split())

# a_reverse = list(a)
# b_reverse = list(b)

# a_reverse.reverse()
# b_reverse.reverse()

# A = int(''.join(a_reverse))
# B = int(''.join(b_reverse))

# if A > B: 
#     print(A)
# else:
#     print(B)

#######################################################
# 11654번 아스키코드

# print(ord(input()))

