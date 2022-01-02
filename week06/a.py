n = 8
# tmp = []

# while n != 0:
#     tmp.append(n%2)
#     n = n//2

# tmp.reverse()
# print(tmp)
# print(*tmp, sep=' ')

def solution(n, r):
    tmp = []
    while n !=0:
        tmp.append(n%r)
        n = n//r
    tmp.reverse()
    new_tmp = ''.join(map(str, tmp))
    return new_tmp

print(solution(5, 3))



