from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]
indegree = [0] * 101 # indegree 101개 설정(문제에서 주어진 장난감 개수가 최대 100개이므로)
v = [[0] * (N+1) for _ in range(N+1)] # 개수를 저장할 배열(2차원) -->왜..
# print(v)
for i in range(M):
    # cur 만들어야할 부품 /prev 사용되는 부품 /val 갯수
    cur, prev, val = map(int, input().rstrip().split())
    graph[prev].append((cur, val))  # 만들때 사용하는 부품 기준으로 필요한 부품갯수 저장
    indegree[cur] += 1  # 차수 만들어야할 부품

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:  # 차수가 0인 기본 부품에서 시작
        q.append(i)
        v[i][i] = 1  # 기본 부품만 시작값을 1로 할당함 -> 1개씩 주고 시작
        # 중간 부품은 0으로 설정 -> 카운트 할 때 제외하려고
        # print(v[i]) # [0, 1, 0, 0, 0, 0, 0, 0]
        # print(v[i][i]) # 1
        
while q:
    now = q.popleft()
    # print(now) #1, 2, 3, 4, 5, 6, 7 순서 
    for next in graph[now]:
        # print(next) --> (5, 2) (5, 2), (6, 3), (6, 4), (7, 5), (7, 2), (6, 2), (7, 3)
        for i in range(1, N+1):
            # 다음 부품 만드는 데 필요한 개수 = 현재 부품 만드는 데 필요한 개수 * 다음 부품 만들 때 필요한 부품
            # 다음 부품 만드는 데 필요한 부품 계산 = 현재 부품 만드는데 드는 개수에 다음 부품 만들때 필요한 부품 곱해줌
            v[next[0]][i] += next[1]*v[now][i]
            # next[0]은 5, 6, 7
            # 5번 부품 만드는데 필요한 i 개수는, 
            # v[now][i] 는 1번 기본부품 만드는데 필요한 개수 : 1개
            # next[1] 은 (5, 2)에서 2를 의미
            # print(v)
        indegree[next[0]] -= 1 # 다음 부품의 진입 차수 -1 ex) 5번 부품의 진입차수 -1 해주기
        if indegree[next[0]] == 0:
            q.append(next[0])

for i in range(1, N+1):
    if v[N][i]:  # 기본 부품 외에 다른건 시작이 0이었기 때문에 세지 않음
        print(f"{i} {v[N][i]}")
