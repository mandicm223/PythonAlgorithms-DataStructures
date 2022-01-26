'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). 
The subsequence must be strictly increasing.
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        anchor = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] >= nums[i]: anchor = i
            result = max(result , i - anchor + 1)
        return result