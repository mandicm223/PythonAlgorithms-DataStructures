'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res , count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += ( 1 if n == res else -1 )
        print(res)

kraj = Solution()
kraj.majorityElement([1,2,3,4])        