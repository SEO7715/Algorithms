import sys
input = sys.stdin.readline

N = int(input())
string_list = []
alphabet_list = {}
group = []

for _ in range(N):
    string_list.append(input().strip())

for i in range(65, 91):
    group.append(chr(i))

for alphabet in group:
    alphabet_list[alphabet] = 0

for i in range(len(string_list)):
    len_string = len(string_list[i])
    for j in range(len_string):
        make_cipher = (10**(len_string - (j+1))) 
        alphabet_list[string_list[i][j]] += make_cipher

alphabet_list = sorted(alphabet_list.items(), key=lambda x:x[1], reverse=True)

adjust_number = 9
answer = 0

for i in alphabet_list:
    if i[1] == 0:
        break
    answer += adjust_number * i[1]
    adjust_number -= 1

print(answer)



