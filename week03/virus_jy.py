import sys

# 컴퓨터의 개수 (Node의 개수)
computer_N = int(sys.stdin.readline().strip())
# 연결의 개수 (간선의 개수)
computer_connect = int(sys.stdin.readline().strip())

# 컴퓨터 연결 상태를 2차원 배열로 저장
network = [[] for _ in range(computer_N + 1)]
print(network)

for i in range(computer_connect):
    com1, com2 = map(int, sys.stdin.readline().strip().split())
    network[com1].append(com2)
    network[com2].append(com1)
print(network)

# virus가 있는지 dfs로 탐색하는 함수
def check_virus(network, start, visited = []):
    visited.append(start)
    for connect_computer in network[start]:
        if connect_computer not in visited:
            check_virus(network, connect_computer, visited)

# net이 2차원 배열인데 (어디랑 어디가 연결됐는지 알려주는) net[start] 하면 start가 어디랑 이어져 있는지 담긴 리스트
# [ [2, 3], [4, 5] ]

    return visited

print(len(check_virus(network, 1, [])) - 1)