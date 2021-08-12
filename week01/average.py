import sys

C = int(sys.stdin.readline())

for i in range(C):
    N = list(map(int, sys.stdin.readline().split()))
    N_avg = sum(N[1:]) / N[0]

    count = 0
    for i in N[1:]:
        if i > N_avg:
            count += 1
            
    t = (count / N[0])*100
    print(f'{t:.3f}%')


# for i in range(C):
#     if N_avg < N[i]:
#         print(N[i])


# print(N_sum, N_avg)

# N[1:] / N[0]

# for i in range(C):
#     N[0], N[1:]



# count = 0

# b = []

# for i in range(9):
#     a = int(sys.stdin.readline())
#     b.append(a)

# for i in range(C):
#    R, S = sys.stdin.readline().split()
#    for i in range(len(S)):
#     print(R, (S, ""))

#    resu = ''
#    for i in range(len(S)):
#       resu += (S[i] * int(R))
#    print(resu)

# for i in range(C):
#     P, S = map(int, sys.stdin.readline().split())
#     print(P, S)


    # score = list(map(int, sys.stdin.readline().split()))
    # average = sum(score[1:]) // score[0]
# # ---> 0번째 값은 학생수니깐..! 없애줘야 함

#     for j in score[1:]:
#         if average < j:
#             count += 1
#     print("%.3f%%"%((count/score[0]))*100)
#     count = 0


