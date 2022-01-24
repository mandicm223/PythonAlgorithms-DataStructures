a = ['1' , '150' , '31415926535897932384626433832795' , '314159265358979323']


def bubble_sort(strings):
    nums = []
    for i in strings:
        nums.append(int(i))
    
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
    return nums


print(bubble_sort(a))