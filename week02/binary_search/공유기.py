import sys 

N, C = map(int, sys.stdin.readline().split())
place_list = [int(sys.stdin.readline()) for _ in range(N)]

place_list.sort()
start = 1 #정수니깐, 1부터 시작
end = place_list[-1] - place_list[0] #최대 길이

while start <= end:
    mid = (start + end) // 2
    status = 1 #공유기 설치(처음 설치하고 시작)
    before_place = place_list[0] #

    for i in range(1, N):
        if place_list[i] >= before_place + mid : #설치 간격 충족
            status += 1
            before_place = place_list[i]

    if status >= C: #주어진 공유기 개수와 설치한 개수 비교
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)