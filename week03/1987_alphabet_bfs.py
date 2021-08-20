import sys

def BFS(arr, R, C):

    maximum = 0
    queue = set([((0,0), arr[0][0])]) 
    # 같은 위치에 같은 문자열을 가진 상황을 중복 확인할 필요 없으므로 set 사용
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        curr, string = queue.pop()
        maximum = max(maximum, len(string))
        for i in range(4):
            next = (curr[0] + dr[i][0], curr[1] + dr[i][1])
            if 0 <= next[0] < R and 0 <= next[1] < C \
                and arr[next[0]][next[1]] not in string:
                queue.add((next, string+arr[next[0]][next[1]]))

    return maximum

R, C = list(map(int, sys.stdin.readline().split()))
arr = [sys.stdin.readline().strip() for _ in range(R)]

print(BFS(arr, R, C))
