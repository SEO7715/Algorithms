import sys
input = sys.stdin.readline

meeting_N = int(input())

meeting_list = [list(map(int, input().strip().split())) for _ in range(meeting_N)]

# 끝나는 시간으로 먼저 정렬한 다음, 시작 시간으로 정렬 해주기
meeting_list = sorted(meeting_list, key=lambda x : (x[1], x[0]))

count = 0
end_point = 0

for meeting in meeting_list:
    if meeting[0] >= end_point:
        count += 1
        end_point = meeting[1]

print(count)