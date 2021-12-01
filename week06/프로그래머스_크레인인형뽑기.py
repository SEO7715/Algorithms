board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
N = len(board)
new_board = [[None] * N for _ in range(N)]
stack_list = []
count = 0

for y in range(len(board)):
    for x in range(len(board)):
        if board[y][x] != 0:
            new_board[x][N-1-y] = board[y][x]

for i in range(len(new_board)):
    new_board[i] = list(filter(None, new_board[i]))

for j in moves:
    try:
        stack_list.append(new_board[j-1].pop())
        if stack_list[-1] == stack_list[-2]:
            stack_list.pop()
            stack_list.pop()
            count += 2
    except:
        pass
