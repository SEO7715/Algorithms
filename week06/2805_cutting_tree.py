import sys
input = sys.stdin.readline

def cutting_tree():
    tree_N, height = map(int, input().split())
    tree_list = list(map(int, input().split()))

    start = 0 
    end = max(tree_list)

    while start <= end:
        mid = (start + end) // 2
        result = 0 # 자른 나무들의 길이 총합
        for tree in tree_list: 
            if tree > mid:
                result += tree - mid
        
        if result == height: # 자른 나무들의 길이 총합이 주어진 나무 높이랑 같은지 확인
            return mid 

        if result > height: # 자른 나무들의 길이 총합이 더 크면, start 지점 오른쪽(큰 쪽)으로 이동
            start = mid + 1
        else:
            end = mid - 1 # 자른 나무들의 길이 총합이 더 크면, start 지점 왼쪽(작은 쪽)으로 이동

    return end

print(cutting_tree())
