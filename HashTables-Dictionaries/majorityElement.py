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
        res , maxCount = 0, 0
        
        values = {}
        for n in nums:
            values[n] = 1 + values.get(n, 0)
            res = n if values[n] > maxCount else res
            maxCount = max(values[n] , maxCount)
        print(values)
        return res
        

            
                
        
        
        