import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    number =  int(input())
    tree_list = list(map(int, input().split()))
    tree_list.sort()
    result = 0

    for i in range(2, number): 
        result = max(result, abs(tree_list[i]-tree_list[i-2])) 
        # 가장 큰 차이 tree_list[i]-tree_list[i-2])

    print(result)
    