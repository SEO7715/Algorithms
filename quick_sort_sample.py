import sys

def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = nums[rt]

        for i in range(lt, rt):
            if nums[i] <= pivot:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        nums[pos], nums[rt] = nums[rt], nums[pos]
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)

n = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(n))

Qsort(0, len(nums) -1)
for n in nums:
    print(n)