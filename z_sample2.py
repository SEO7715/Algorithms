# 시간초과
import sys


n, r, c = map(int, sys.stdin.readline().split())
count = 0

def recursion(size, start_row, start_col):
    global count
    if size == 2:
        if r == start_row and c == start_col: #1사분면
            print(count)
            return
        count += 1
        if r == start_row and c == start_col + 1: #2사분면
            print(count)
            return
        count += 1    
        if r == start_row + 1 and c == start_col: #3사분면
            print(count)
            return
        count += 1 
        if r == start_row + 1 and c == start_col + 1: #4사분면
            print(count)
            return
        count += 1
    else: 
        recursion(size//2, start_row, start_col) #1사분면
        recursion(size//2, start_row, start_col + size//2) #2사분면
        recursion(size//2, start_row + size//2, start_col) #3사분면
        recursion(size//2, start_row + size//2, start_col + size//2) #4사분면

recursion(2**n, 0, 0) 