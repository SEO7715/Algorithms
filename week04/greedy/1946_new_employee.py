import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    applicants = int(input())
    scores = [list(map(int, input().strip().split())) for _ in range(applicants)]
    scores.sort(key=lambda x : x[0]) # 서류 성적 순으로 정렬

# 서류 성적 1위의 경우, 면접 등수에 관계없이 합격이므로
# 서류 성적 1위의 면접 순위를 기준으로 비교
    cnt = 1
    interview_standard = scores[0][1]

    for score in scores:
        if score[1] < interview_standard:
            cnt += 1
            interview_standard = score[1]

    print(cnt)
