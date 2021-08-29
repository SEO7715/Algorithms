import sys
input = sys.stdin.readline

item_number, support_weight = map(int, input().strip().split())

dp = [0] * (support_weight + 1) # dp 탐색을 위해 초기 설정한 arr # 지탱할 수 있는 무게 만큼 dp 생성
# print(dp) # [0, 0, 0, 0, 0, 0, 0, 0]

item_list = [] # 아이템별 무게, 가치 저장 위한 배열

for _ in range(item_number):
    weight, value = map(int, sys.stdin.readline().strip().split())
    item_list.append((weight, value))

# print(item_list) # [(6, 13), (4, 8), (3, 6), (5, 12)]

for i in range(item_number): # i는 0 1 2 3
    for j in range(support_weight, 0, -1): # j는 7 6 5 4 3 2 1 (역순으로 해야함, 순서대로 담게 되면 중복으로 넣는 경우가 생기게 됨)
        if j - item_list[i][0] >= 0: # 예외처리 
            # j가 item_list[i][0]보다 같거나 클 때
            dp[j] = max(dp[j], dp[j - item_list[i][0]] + item_list[i][1])


# print(dp) # [0, 0, 0, 6, 8, 12, 13, 14]

print(dp[support_weight])