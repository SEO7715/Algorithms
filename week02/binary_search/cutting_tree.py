import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)

while start <= end:
    # trees.sort() --> 중간값을 활용하는 게 아니므로 여기선 안해줘도 됨
    mid = (start + end) // 2
    result = 0 
    for tree in trees:
        if tree > mid:
            result += tree - mid
    
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end) # 절단기 높이 최댓값

