import sys

# N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2 # 중간지점 
    low_array = merge_sort(array[:mid]) #시작부터 중간
    high_array = merge_sort(array[mid:]) #중간부터 끝

    merged_array = []
    l = h = 0 
    while l < len(low_array) and h < len(high_array):
        if low_array[l] < high_array[h]: #더 작은 값을 추가해줌
            merged_array.append(low_array[l])
            l += 1
        else: #더 작은 값을 추가해줌
            merged_array.append(high_array[h])
            h += 1
    
    merged_array += low_array[l:]
    merged_array += high_array[h:]
    return merged_array

merge_sort(array)
for n in array:
    print(n)