import sys
input = sys.stdin.readline

def cutting_tree():
    tree_N, height = map(int, input().split())
    tree_list = list(map(int, input().split()))

    start = 0 
    end = max(tree_list)

    while start <= end:
        mid = (start + end) // 2
        result = 0 
        for tree in tree_list: 
            if tree > mid:
                result += tree - mid
        
        if result == height:
            return mid 

        if result > height: 
            start = mid + 1
        else:
            end = mid - 1 

    return end

print(cutting_tree())