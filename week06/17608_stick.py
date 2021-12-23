import sys
input = sys.stdin.readline

case_N = int(input())
stick_list = []

for _ in range(case_N):
    stick_list.append(int(input()))

max_stick = stick_list[-1]
cnt = 1

for _ in range(case_N):
    compare_stick = stick_list.pop()
    if max_stick < compare_stick:
        cnt += 1
        max_stick = compare_stick
        
print(cnt)