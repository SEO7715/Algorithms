nums = [3,3,3,2,2,2]

def solution(nums):
    only_nums = set(nums)
    if len(only_nums) <= (len(nums) // 2):
        result = len(only_nums)
    else:
        result = len(nums) // 2
    return result

print(solution(nums))