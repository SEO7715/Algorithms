import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
array = [int(x) for x in sys.stdin.readline().split()]
array.sort()

def get_Number(arr):
    i, j = 0, len(arr) - 1
    min_value = abs(arr[i] + arr[j])
    min_set = i, j
    while i < j:
        current = arr[i] + arr[j] #현재값
        if abs(current) < min_value: #현재값(절대값)이 최소값으로 설정한 값보다 작으면
            min_value = abs(current) #현재값으로 최소값 설정해주기
            min_set = i, j
            
        if current == 0: #현재값이 0이라면, 정답처리
            return min_set
        elif current > 0: #현재값(절대값)이 0보다 크면 오른쪽으로 범위 이동
            j -= 1
        else:
            i += 1
    return min_set

a, b = get_Number(array)
print(array[a], array[b])
