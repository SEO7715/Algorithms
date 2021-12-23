a, b = map(int, input().strip().split())


## ver1
# for _ in range(b):
#     for _ in range(a):
#         print('*', end= "")
#     print('')

#ver2
answer = ('*'*a + '\n')*b
print(answer)