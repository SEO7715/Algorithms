import sys
from itertools import permutations 

people = [int(sys.stdin.readline()) for i in range(9)]
sum_people = sum(people)

# 또는
# people = []
# for i in range(9):
#     people.append(int(input()))

except_case = list(permutations(people, 2))

for i in range(len(except_case)):
    if (except_case[i][0] + except_case[i][1]) == (sum_people - 100):
        people.remove(except_case[i][0])
        people.remove(except_case[i][1])
        break

final_people = sorted(people)

for person in final_people:
    print(person)