import sys
input = sys.stdin.readline

N = int(input())

cost_list = []
for _ in range(N):
    cost_list.append((list(map(int, input().strip().split()))))

memo = [[0]*N for _ in range(N+1)]
# print(memo) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(N-1, -1, -1):
    # print(i) # 2 1 0
    for color in range(3):
        min_subscore = float("inf")
        for other in range(3):
            if color != other:
                min_subscore = min(min_subscore, memo[i+1][other]) 
        memo[i][color] = cost_list[i][color] + min_subscore

# 4단계: 본래의 문제 해결
# - 인덱스 0번째 집을 R, G, B 중 하나로 시작하는 비용 중 최소값 출력
min_score = min(memo[0])
print(min_score)