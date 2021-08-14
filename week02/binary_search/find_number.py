# 바이너리 서치 구현
def binary_search(target, data):
    data.sort() #정렬된 데이터
    start = 0
    end = len(data) -1

    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid #함수 종료
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None 

if __name__ == "__main__":
    list = [i**2 for i in range(11)]
    target = 25
    idx = binary_search(target, list)

    if idx:
        print(list[idx])

    else:
        print("찾는 타겟 {}가 없습니다.".format(target))

# 바이너리 서치 재귀적 구현
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid -1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)

if __name__ == '__main__':
    list = [i**3 for i in range(11)]
    target = 125
    idx = binary_search_recursion(target, 0, 10, list)

    print(list)
    print(idx)