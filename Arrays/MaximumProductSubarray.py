'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''

def maximunSubarray(nums):
    res = max(nums)

    curMin , curMax = 1 , 1
    for n in nums:
        if n == 0:
            curMin , curMax = 1 , 1
        
        tmp = curMax * n
        curMax = max(curMax * n , curMin * n , n)
        curMin = min(tmp , curMin * n , n)
        res = max(res , curMin , curMax)
    return res

    