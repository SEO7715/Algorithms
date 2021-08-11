# 알고리즘 문제 테스트 하는 공간
import sys
import copy
sys.setrecursionlimit(10**9)

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
​
maxNum = 0
land = 0
​
for t in range(len(data)):
    for y in range(len(data[t])):
        if data[i][t] > maxNum:
            maxNum = data[i][t]
​
​
def numIslands(land, rain) -> int:
    global maxNum
    if maxNum == 1 and rain >= 1:
        return 0
    count = 0
    checkLand = copy.deepcopy(land)
    for i in range(len(checkLand)):
        for j in range(len(checkLand[0])):
            if checkLand[i][j] != 0 and checkLand[i][j] > rain:
                count += 1
                visit(i, j, checkLand, rain)
        # print('---------------------------')
        # for b in range(len(checkGrid)):
        #     print(checkGrid[b])
        # print('---------------------------')
        # print(count)
        # print('###########################')
    return count
​

def visit(i, j, checkLand, rain):
    if i >= len(checkLand):
        return
    if j >= len(checkLand[0]):
        return
    if i < 0:
        return
    if j < 0:
        return
    if checkLand[i][j] <= rain:
        return
    checkLand[i][j] = 0
    visit(i + 1, j, checkLand, rain)
    visit(i, j + 1, checkLand, rain)
    visit(i - 1, j, checkLand, rain)
    visit(i, j - 1, checkLand, rain)

​
answer = []
for rain in range(0, maxNum):
    check = numIslands(data, rain)
    if check > land:
        land = check
​
print(land)