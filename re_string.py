# 2675번 (문자열 반복)
import sys

P = int(sys.stdin.readline())

for i in range(P):
   R, S = sys.stdin.readline().split()
   resu = ''
   for i in range(len(S)):
      resu += (S[i] * int(R))
   print(resu)
    