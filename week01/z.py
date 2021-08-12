import sys

n, r, c = map(int, sys.stdin.readline().split())

def find_part():
    if 0 <= r < 2**(n-1) and 0 <= c < 2**(n-1):
        print('1분면')
    elif 0 <= r < 2**(n-1) and 2**(n-1) <= c < 2**n:
        print('2분면')
    elif 2**(n-1) <= r < 2**n and 0 <= c < 2**(n-1):
        print('3분면')
    else:
        print('4분면')

part = (2**(n-1)) * (2**(n-1))





