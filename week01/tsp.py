import sys
from itertools import permutations 

people = [int(sys.stdin.readline()) for i in range(9)]
sum_people = sum(people)


# import sys 

# N = int(sys.stdin.readline())

# pos = [0] * N 
# flag_a = [False] * N 
# flag_b = [False] * (2*N-1) 
# flag_c = [False] * (2*N-1) 

# def put(): 
#     for i in range(N):
#         print(f'{pos[i]:2}', end='')
#     print()

# def set(i: int):
#     for j in range(N):
#         if (not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (N-1)]):
#             pos[i] = j
#             if j == (N-1):
#                 put()
#             else:
#                 flag_a[j] = flag_b[i +j] + flag_c[i - j + (N-1)] = True
#                 set(i + 1)
#                 flag_a[j] = False

# set(N)
# print(len(set()))