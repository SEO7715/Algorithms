import sys

N = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))
solution.sort()

left = 0
right = len(solution) -1
sum_solution = []

while left < right:
    sum = solution[left] + solution[right]
    tmp = [solution[left], solution[right], abs(sum)]
    sum_solution.append(tmp)
    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

sum_solution.sort(key= lambda x: x[2])
print(sum_solution[0][0], sum_solution[0][1])