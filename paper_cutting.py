import sys

x, y = map(int, sys.stdin.readline().split())

c = int(sys.stdin.readline())

A = [0]
B = [0]

for i in range(c):
    s = list(map(int, sys.stdin.readline().split()))
    if (s[0] == 0):
        A.append(s[1])
    else :
        B.append(s[1])

max_x = [0]
max_y = [0]

for i in range(len(A)):
    if A[i] > (y - sum(A) or sum(A)):
        max_x = A[i]
    elif y - sum(A) > (A[i] or sum(A)):
        max_x = y - sum(A)
    else:
        max_x = sum(A)

print(sum(A), max_x)


for i in range(len(B)):
    if B[i] < x - sum(B):
        max_y = x - sum(B)
    else:
        max_y = B[i]

# print(max_x, max_y)