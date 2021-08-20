import sys

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(sys.stdin.readline())

alpha = [False] * 26
alpha[ord(board[0][0])-65] = True

maxCount = 0

def dfs(x, y, al, count):
    global maxCount

    maxCount = max(maxCount, count)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R:
            c = ord(board[ny][nx]) - 65
            if not al[c]:
                al[c] = True
                dfs(nx, ny, al, count+1)
                al[c] = False

dfs(0, 0, alpha, 1)
print(maxCount)
