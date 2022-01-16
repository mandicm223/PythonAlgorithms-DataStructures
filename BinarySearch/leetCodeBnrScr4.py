class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = []
        for num in range(0 , x):
            nums.append(num)
            
        
        lo = 1
        hi = x
        
        if x < 2:
            return x
        
        while lo < hi:
            mid = ( lo + hi ) // 2
            
            if nums[mid] * nums[mid] == x:
                return mid
            if nums[mid] * nums[mid] < x:
                if nums[mid + 1] * nums[mid + 1] > x:
                    return mid
                lo = mid + 1
            else:
                if nums[mid - 1] * nums[mid - 1] < x:
                    return mid
                hi = mid - 1

proba = Solution()
print(proba.mySqrt(10))