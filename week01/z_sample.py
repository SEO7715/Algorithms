import sys

n, r, c = map(int, sys.stdin.readline().split())

def recursion(start_row, end_row, start_col, end_col, n):
    
    if r == start_row and  c == start_col:
        print(n)
        return
    
    mid_row = (start_row + end_row) //2
    mid_col = (start_col + end_col) //2

    part_size = (mid_row - start_row)  * (mid_col - start_col)

    if start_row <= r < mid_row and start_col <= c < mid_col:
        recursion(start_row, end_row, start_col, end_col, n)
    elif mid_row <= r < end_row and start_col <= c < mid_col:
        recursion(start_row, end_row, start_col, end_col, n + part_size)
    elif start_row <= r < mid_row and mid_col <= c < end_col:
        recursion(start_row, end_row, start_col, end_col, n + (2 * part_size))
    else:
        recursion(start_row, end_row, start_col, end_col, n + (3 * part_size))

recursion(0, 2**n, 0, 2**n, 0)
