import sys
from collections import deque, defaultdict

def minimum_coins():

	# input
    n, target = list(map(int, sys.stdin.readline().split()))
    coins = [None] * n
    for i in range(n):
        coins[i] = int(sys.stdin.readline())
    coins = sorted(set(coins), reverse=True)

    queue = deque([(1, target - coin) for coin in coins])

    visited = defaultdict(lambda: False)
    #defaultdict --> 호출과 동시에 미리 지정한 기본값 할당 가능

	# BFS
    while queue: # 큐가 빌 때까지
        level, target = queue.popleft()
        if visited[target]: # 방문 내역이 있으면 제외
            continue

		# base cases
        visited[target] = True

        if target < 0:
            continue
        elif target == 0:
            return level
        
		# 계속 탐색
        for coin in coins:
            queue.append((level+1, target - coin)) 

    return -1
print(minimum_coins())