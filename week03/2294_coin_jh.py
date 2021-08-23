import sys
from collections import deque, defaultdict

def minimum_coins():

	# input
    n, target = list(map(int, sys.stdin.readline().split()))
    coins = [None] * n
    for i in range(n):
        coins[i] = int(sys.stdin.readline())
    coins = sorted(set(coins), reverse=True)
    # print(coins) #[12, 5, 1]

    queue = deque([(1, target - coin) for coin in coins])
    # print(queue) # deque([(1, 3), (1, 10), (1, 14)])
    # visited = False
    visited = defaultdict(lambda: False)
    #defaultdict --> 호출과 동시에 미리 지정한 기본값 할당 가능

	# BFS
    while queue: # 큐가 빌 때까지
        level, target = queue.popleft()
        # print(queue.popleft()) --> #(1,10)(2,-9)(2,2)(3,-10)(3,1)(3,8)(4,-11)(4,0)(4,7)... 왜..이렇게 나오지..?
        # print(visited[target])
        if visited[target]: # 방문 내역이 있으면 제외( visited[target]이 True면 )
            # print(visited[target]) # True
            continue
		# print(visited[target]) # 왜 여기선..인식이 안되는거지

		# base cases
        visited[target] = True
        # print(visited[target])

        if target < 0:
            continue
        elif target == 0:
            return level
        
		# 계속 탐색
        for coin in coins:
            queue.append((level+1, target - coin)) 

    return -1
print(minimum_coins())