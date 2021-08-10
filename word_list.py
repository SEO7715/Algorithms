import sys

N = int(sys.stdin.readline())
word_list = []

for x in range(N):
    word_list.append(sys.stdin.readline().rstrip()) #input은 rstrip안해도 개행문자 제거해줌
    # word_list[x] = word_list[x].rstrip('\n')

word_list = sorted(set(word_list))
word_list.sort(key=len)

for word in word_list:
    print(word)

