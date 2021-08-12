import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
array = []

for x in range(N):
    tmp = int(sys.stdin.readline())
    array.append(tmp)

def Qsort (array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫번째 원소
    left = start + 1
    right = end

    while(left <= right): #left가 right보다 같거나 작을 때 (커지면, 정렬 완료된 것이므로)
        while(left <= end and array[left] <= array[pivot]): 
            #end(right)보다 left 값이 같거나 작으면서, array[left] 값이 array[pivot] 값보다 같거나 작으면 //
            #피벗보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while(right > start and array[right] >= array[pivot]): 
            #start(pivot)보다 end(right)가 크면서, array[right] 값이 array[pivot] 값보다  크거나 같으면 //
            #피벗보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if(left > right): #right 보다 left가 크면(이미 교차했거나, 같은 상태) --->????
            array[right], array[pivot] = array[pivot], array[right] #엇갈렸을 경우, 작은 데이터와 피벗 교체
        else:
            array[left], array[right] = array[right], array[left] #엇갈리지 않았을 경우, 작은 데이터와 큰 데이터 교체 
        
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    Qsort(array, start, right -1)
    Qsort(array, right + 1, end)

Qsort(array, 0, len(array) -1)

for x in array:
    print(x)

    