import sys
input = sys.stdin.readline

N, B = map(int,input().split())

Matrix=[list(map(lambda x: x % 1000, map(int, input().split()))) for _ in range(N)]

def multiply(A, B):   # N X N Matrix A, B의 곱
    N = len(Matrix)
    C = [[0] * N for j in range(N)]

    for i in range(N):
        for j in range(N):
            component = 0
            for k in range(N):
                component += A[i][k] * B[k][j]
                print(component)
            C[i][j] = component % 1000
    return C

def multiply2(Matrix, n):
    if n == 1:
        return Matrix

    temp = multiply2(Matrix, n//2) # 분할하여 곱해주기 위해서 

    if n % 2==0:
        return multiply(temp, temp)

    else:
        return multiply(multiply(temp,temp), Matrix)

answer = multiply2(Matrix, B)

for i in range(N):
    print(' '.join(map(str,answer[i])))