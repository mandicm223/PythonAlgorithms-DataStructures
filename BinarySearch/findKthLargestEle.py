'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

def findKthLargest(nums , k):
    k = len(nums) - k

    def quickSelect(l , r):
        pivot , p = nums[r] , l

        for i in range(l , r):
            if nums[i] <= pivot:
                nums[i] , nums[p] = nums[p] , nums[i]
                p += 1
        nums[r] , nums[p] = nums[p] , nums[r]

        if p > k: return quickSelect(l , p - 1)
        elif p < k: return quickSelect(p+1 , r)
        else: return nums[p]
    return quickSelect(0 , len(nums) -1) 