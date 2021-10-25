import sys
input = sys.stdin.readline

N = input()
N_list = list(map(int, input().split()))
N_list.sort()
M = input()
target_list = list(map(int, input().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for target in target_list:
    if binary_search(target, N_list):
        print(1)
    else:
        print(0)

