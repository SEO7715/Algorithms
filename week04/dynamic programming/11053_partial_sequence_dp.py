import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

length = [0] * n
# print(length)  # [0, 0, 0, 0, 0, 0]

for i in range(n):
    # print(length[i]) # 0 0 0 0 0
    # print(i)  # i는 0, 1, 2, 3, 4, 5
    length[i] = 1 # 초기 길이값 1로 설정
    for j in range(i):
        if num[j] < num[i]:
            length[i] = max(length[i], length[j] + 1)
    print(length[i])
print(max(length))