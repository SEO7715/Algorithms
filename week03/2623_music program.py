import sys
import collections

# 가수 수, 보조pd 수 입력 받기
singer_N, subpd_N = map(int, sys.stdin.readline().strip().split())

singer_order = [[] for _ in range(singer_N + 1)] # 가수 수 범위 만큼 2차원 리스트 만들기 [[], [], [], [], [], [], []]

indegree = [0] * (singer_N + 1) # 진입차수 0으로 초기화

queue = collections.deque()

# 보조 pd들의 순서를 singer_order이라는 전체 2차원 배열에 저장.
for _ in range(subpd_N): # 보조pd 수 범위 내 for문 
    sub_order = list(map(int, sys.stdin.readline().strip().split())) # 보조 pd 순서 입력 받기 
    for i in range(1, sub_order[0]): # 1부터 총 가수 수 범위 내(1부터 마지막 부분까지)
        singer_order[sub_order[i]].append(sub_order[i + 1]) # sub_order[i]에서 sub_order[i+1]로 이동 가능
        indegree[sub_order[i + 1]] += 1 # 해당 노드의 진입차수 +1

for i in range(1, singer_N + 1): # 1부터 N까지 범위 내 i 에 대해 
    if indegree[i] == 0: # 진입차수 0일 경우
        queue.append(i) # q에 추가

# 일반적인 위상정렬 방식. 진입차수가 0인 노드를 제거하고, 그 노드와 연결된 노드들의 진입차수를 1씩 낮춘다. 
# 그리고 다시 진입차수가 0이 된 노드를 queue에 추가한다.

fixed_order = [] # 수행 결과를 담을 리스트
while queue:
    start_node = queue.popleft()
    fixed_order.append(start_node)
    for node in singer_order[start_node]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

# 가수의 수만큼 fixed_order에 담기지 않았다면,
# 순환 부분이 있다는 것이므로, 0 출력!
if len(fixed_order) != singer_N: 
    print(0)
else:
    for singer in fixed_order:
        print(singer)