import sys

array = list(map(int, sys.stdin.readline().split()))


def Qsort (array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫번째 원소
    left = start + 1
    right = end
    # print(array[left])
    print(left)

    while(left <= right):
        while(left <= end and array[left] <= array[pivot]): #피벗보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while(right > start and array[right] >= array[pivot]): #피벗보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right] #엇갈렸을 경우, 작은 데이터와 피벗 교체
        else:
            array[left], array[right] = array[right], array[left] #엇갈리지 않았을 경우, 작은 데이터와 큰 데이터 교체 
        
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    Qsort(array, start, right -1)
    Qsort(array, right + 1, end)

Qsort(array, 0, len(array) -1)
print(array)

    