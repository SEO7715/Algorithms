import sys
input = sys.stdin.readline

N = int(input()) # 보드크기
matrix = [[0]* N+1 for _ in range(N+1)] # 0으로 기본 설정
# print(matrix)

for _ in range(int(input())): # 사과 위치
    a, b = map(int, input().split())
# print(a, b)

L = int(input()) # 방향
L_array = list(map(lambda x:[int(x[0]), x[1]], [input().split() for _ in range(L)]))
# print(L_array)

x, y = 0, 0 # 뱀 시작 위치

d = [(0,1), (1,0), (0,-1), (-1,0)] # 동 남 서 북

count = 0 # 이동시간

# def move(x, y):
#     if x == "L":

#     elif x == "D":


