N = int(input())

def 왕재수(n):
    if n == N+1:
        print(0)
        return
    print(2*(N-n+1))
    왕재수(n+1)
    print(4*(N-n+1))

왕재수(1)