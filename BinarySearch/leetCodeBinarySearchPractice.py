def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = ( lo + hi ) // 2
        result = condition(mid)
        
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1
            
def find_strting_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums) -1,condition)

def find_last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid + 1] == target:
                return "right"
            else:
                return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums) - 1,condition)

def first_and_last_position(nums, target):
    return find_strting_position(nums, target), find_last_position(nums, target)

def searchRange(nums, target):
    return first_and_last_position(nums, target) 

numbers = [5,7,8,8,8,8,10]
taregtt = 8

print(searchRange(numbers, taregtt))
        