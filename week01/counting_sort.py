import sys

N = int(sys.stdin.readline())
array = [0] * 10001

for i in range(N):
    array[int(sys.stdin.readline())] += 1

def merge_sort(array, max):
    n = len(array)
    f = [0] * (max + 1)
    b = [0] * n

    for i in range(n): #1단계 도수분포표 만들기
        f[array[i]] += 1
    
    for i in range(1, max + 1): #누적 도수분포표 만들기
        f[i] += f[i-1]

    for i in range(n-1, 0-1, -1): #작업용 배열 만들기
        f[array[i]] -= 1
        b[f[array[i]]] = array[i]
    
    for i in range(n): # 배열 복사하기
        array[i] = b[i]

def counting_sort(array):
    merge_sort(array, max(array))

print(array)

    

    