def binary_search(nums,target):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        curSum = nums[lo] + nums[hi]

        if curSum == target:
            return lo + 1, hi + 1
        elif curSum > target:
            hi -= 1
        else:
            lo += 1



nums = [2,7,11,15]
target = 9
print(binary_search(nums,target))