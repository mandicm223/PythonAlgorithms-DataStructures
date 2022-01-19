'''
Problem #1
Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

 
For example,

Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
Output: { 0, 0, 0, 0, 1, 1, 1, 1 }
'''

def quick_sort(nums , start=0, end = None):
    if end is None:
        end = len(nums) - 1
    
    if start < end:
        pivot = partitioning(nums , start , end)
        quick_sort(nums , start , pivot - 1)
        quick_sort(nums , pivot + 1 , end)
    return nums

def partitioning(nums , start , end=None):
    if end is None:
        end = len(nums) - 1
    
    l , r = start , end -1

    while l < r:
        
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l] , nums[r] = nums[r] , nums[l]
    if nums[l] > nums[end]:
        nums[end] , nums[l] = nums[l] , nums[end]
        return l
    else:
        return end

print(quick_sort([1, 0, 1, 0, 1, 0, 0, 1 ]))