# 8958번 (ox퀴즈)

import sys

C = int(sys.stdin.readline())

score_list = []

for i in range(C):
    count = 0
    score = 0
    case_list = sys.stdin.readline()
    for case in case_list:
        if case == 'O':
            count += 1
        else:
            count = 0
        score += count
    score_list.append(score)

for score in score_list:
    print(score)

