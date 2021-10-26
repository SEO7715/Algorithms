import sys
input = sys.stdin.readline

test_case = int(input())

while test_case:
    A, target = map(int, input().split())
    A_list = list(map(int, input().split()))
    target_list = list(map(int, input().split()))
    A_list.sort()
    target_list.sort()

    count = 0
    for i in A_list:
        for target in target_list:
            if i > target:
                count += 1

    print(count)
    test_case -= 1

##### bisect ver #####

# import sys
# import bisect

# input = sys.stdin.readline

# t = int(input())

# while t:

#     cnt = 0

#     n, m = map(int, input().split())

#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
    
#     A.sort()
#     B.sort()

#     for i in A:
#         cnt += bisect.bisect_left(B, i)
    
#     print(cnt)
#     t-=1