import sys

M, N, L= map(int, sys.stdin.readline().split()) # M 사대수, N 동물 수, L 사정거리
place_list = list(map(int, sys.stdin.readline().split())) # 사대위치
place_list.sort()

animal= [list(map(int, sys.stdin.readline().split())) for i in range(N)] #동물위치

count = 0
for a, b in animal:
    start = 0
    end = len(place_list)-1
    while start < end:
        mid = (start + end) // 2
        if place_list[mid] < a:
            start = mid + 1
        else:
            end = mid #왜..?
    if abs(place_list[end]-a)+b <= L or abs(place_list[end-1]-a)+b <= L: #왜..?
        count += 1

print(count)


