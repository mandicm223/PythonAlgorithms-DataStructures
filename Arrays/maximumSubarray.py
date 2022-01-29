'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

def maxsubarray(nums):
    maxSum = nums[0]
    curSum = 0

    for i in nums:
        if curSum < 0:
            curSum = 0
        
        curSum += i
        maxSum = max(maxSum , curSum)
    return maxSum



