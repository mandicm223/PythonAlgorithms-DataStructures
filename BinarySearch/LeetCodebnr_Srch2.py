def return_index(nums,index):
    lo  = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = ( hi + lo ) // 2

        if nums[mid] == index:
            return mid
        elif nums[mid] < index:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

print(return_index([1,3,5,6], 8))