# sort() 
original_List = [1, 2, 44, 52, 61, 7, 28, 92, 10]
original_List.sort()

print(original_List)

# sort(reverse=True) 
reverse_List = [1, 2, 44, 52, 61, 7, 28, 92, 10]
reverse_List.sort(reverse=True)

print(reverse_List)

# sort()의 key 옵션

a = '파이썬 공부 sort 함수 부분'
a = a.split()
a.sort(key=len)
print(a)