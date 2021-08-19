import sys
input = sys.stdin.readline

k, n = map(int, input().split())
prime_number_list = list(map(int, input().split()))

case_list = []

for i in prime_number_list:
    case_list.append(i)
    case_list.append(i*i)
    for j in prime_number_list:
        case_list.append(i)
        case_list.append(i*i)
        case_list.append(i*j)

total_list = sorted(set(case_list))
print(total_list)

