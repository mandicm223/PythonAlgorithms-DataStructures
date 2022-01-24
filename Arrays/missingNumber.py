'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i]) 
        return res