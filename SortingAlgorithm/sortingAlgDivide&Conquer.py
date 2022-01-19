from math import e
from jovian.pythondsa import evaluate_test_cases

'''
Problem
In this notebook, we'll focus on solving the following problem:

QUESTION 1:

You're working on a new feature on Jovian called "Top Notebooks of the Week". 
Write a function to sort a list of notebooks in decreasing order of likes. 
Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.

The problem of sorting a list of objects comes up over and over in computer science and software development, 
and it's important to understand common approaches for sorting, and the trade-offs they offer. 
Before we solve the above problem, we'll solve a simplified version of the problem:

QUESTION 2:

Write a program to sort a list of numbers.

"Sorting" usually refers to "sorting in ascending order", unless specified otherwise.
'''


'''
1. State the problem clearly. Identify the input & output formats.
Problem
We need to write a function to sort a list of numbers in increasing order.

Input
nums: A list of numbers e.g. [4, 2, 6, 3, 4, 6, 2, 1]
Output
sorted_nums: The sorted version of nums e.g. [1, 2, 2, 3, 4, 4, 6, 6]
The signature of our function would be as follows:
'''

def sort(nums):
    pass

'''
2. Come up with some example inputs & outputs.
Here are some scenarios we may want to test out:

1. Some list of random nums
2. Some list sorted in decreasing order
3. Empty list
4. Already sorted list
5. List that contains one number many times
6. List that is really long
7. List containing only one element
8. List containing repeating elements 
'''

test0 = {
    'input': {
        'nums' : [4,2,6,3,4,6,2,1]
    },
    'output' : [1 , 2 , 2, 3, 4, 4, 6, 6]
}

test1 = {
    'input': {
        'nums' : [7,6,5,4,3,2,1]
    },
    'output' : [1 , 2 , 3, 4, 5, 6, 7]
}

test2 = {
    'input': {
        'nums' : []
    },
    'output' : []
}

test3 = {
    'input': {
        'nums' : [1,2,3,4,5,6,7]
    },
    'output' : [1,2,3,4,5,6,7]
}


test4 = {
    'input': {
        'nums' : [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output' : [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test5 = {
    'input': {
        'nums' : in_list
    },
    'output' : out_list
}

test6 = {
    'input': {
        'nums' : [5]
    },
    'output' : [5]
}


test7 = {
    'input': {
        'nums' : [42, 42, 42, 42, 42, 42, 42]
    },
    'output' : [42, 42, 42, 42, 42, 42, 42]
}

test8 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}


tests = [test0 , test1 , test2 , test3, test4  , test5 , test6 , test7, test8]


'''
3. Come up with a correct solution. State it in plain English.
It's easy to come up with a correct solution. Here's one:

Iterate over the list of numbers, starting from the left
Compare each number with the number that follows it
If the number is greater than the one that follows it, swap the two elements
Repeat steps 1 to 3 till the list is sorted.
We need to repeat steps 1 to 3 at most n-1 times to ensure that the array is sorted. Can you explain why? Hint: 
After one iteration, the largest number in the list.

This method is called bubble sort, as it causes smaller elements to bubble to the top and larger to sink to the bottom. 

'''

def bubble_sort(nums):
    nums = list(nums)

    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
    return nums

#evaluate_test_cases(bubble_sort, tests)


'''
5. Analyze the algorithm's complexity and identify inefficiencies
The core operations in bubble sort are "compare" and "swap". To analyze the time complexity, \
we can simply count the total number of comparisons being made, 
since the total number of swaps will be less than or equal to the total number of comparisons (can you see why?).

for _ in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
There are two loops, each of length n-1, where n is the number of elements in nums. 
So the total number of comparisons is  (𝑛−1)∗(𝑛−1)  i.e.  (𝑛−1)2  i.e.  𝑛2−2𝑛+1 .

Expressing this in the Big O notation,
we can conclude that the time complexity of bubble sort is  𝑂(𝑛2)  (also known as quadratic complexity).

Exercise: Verify that the bubble sort requires  𝑂(1)  additional space.

The space complexity of bubble sort is  𝑂(𝑛) , even thought it requires only constant/zero additional space, 
because the space required to store the inputs is also considered while calculating space complexity.

As we saw from the last test, a list of 10,000 numbers takes about 12 seconds to be sorted using bubble sort. 
A list of ten times the size will 100 times longer i.e. about 20 minutes to be sorted, which is quite inefficient. 
A list of a million elements would take close to 2 days to be sorted.

The inefficiency in bubble sort comes from the fact that we're shifting elements by at most one position at a time.
'''

'''
Insertion Sort
Before we look at explore more efficient sorting techniques, 
here's another simple sorting technique called insertion sort, 
where we keep the initial portion of the array sorted and insert the remaining elements one by one at the right position.
'''

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1 , cur)
    return nums



'''
6. Apply the right technique to overcome the inefficiency. Repeat Steps 3 to 6.
To performing sorting more efficiently, we'll apply a strategy called Divide and Conquer, which has the following general steps:

Divide the inputs into two roughly equal parts.
Recursively solve the problem individually for each of the two parts.
Combine the results to solve the problem for the original inputs.
Include terminating conditions for small or indivisible inputs.
'''

'''
This is example of how should you implement merging of two sorted lists
'''

def merge_sort_sorted_arrays(a , b):
    sorted_array = []
    i =0
    j = 0
    arr = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1
    tails_a = a[i:]
    tails_b = b[j:]
    return arr + tails_a + tails_b
print(merge_sort_sorted_arrays([1,2,4,5,6] , [3 , 7 , 9,10]))


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)

    sorted_nums = merge_sort_sorted_arrays(left_sorted , right_sorted)
    return sorted_nums


#evaluate_test_cases(merge_sort , tests)


'''
Time complexity

Counting from the top and starting from 0, 
the  𝑘𝑡ℎ  level of the above tree involves  2𝑘  invocations of merge with sublists of size roughly  𝑛/2𝑘 , 
where  𝑛  is the size of the original input list. Therefore the total number of comparisons at each level of the tree is  2𝑘∗𝑛/2𝑘=𝑛 .

Thus, if the height of the tree is  ℎ , the total number of comparisons is  𝑛∗ℎ . Since there are  𝑛  sublists of size 1 at the lowest level,
it follows that  2(ℎ−1)=𝑛  i.e.  ℎ=log𝑛+1 . Thus the time complexity of the merge sort algorithms is  𝑂(𝑛log𝑛) .

As we already saw, it took just 50 ms to sort an array of 10,000 elements. 
Even an array of 1 million elements will take only a few seconds to be sorted.


Space Complexity

since the original sublists can be discarded after the merge operation, the additional space can be freed or reused for future merge calls. 
Thus, merge sort requires  𝑂(𝑛)  additional space i.e. the space complexity is  𝑂(𝑛) .
'''

'''
Quicksort
To overcome the space inefficiencies of merge sort, we'll study another divide-and-conquer based sorting algorithm called quicksort, 
which works as follows:

-If the list is empty or has just one element, return it. It's already sorted.

-Pick a random element from the list. This element is called a pivot.

-Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, 
while all elements with values greater than the pivot come after it. This operation is called partitioning.

-The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.
'''

def quick_sort(nums , start=0 , end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums , start , end)
        quick_sort(nums , start , pivot - 1)
        quick_sort(nums , pivot + 1 , end)
    return nums

def partition(nums , start , end=None):
    if end is None:
        end = len(nums) - 1
    
    l , r = start , end - 1

    while r > l:
        if nums[l] <= nums[end]:
            l += 1

        elif nums[r] > nums[end]:
            r -= 1

        else:
            nums[l] , nums[r] = nums[r] , nums[l]

    if nums[l] > nums[end]:
        nums[l] , nums[end] = nums[end] , nums[l]

        return l
    else:
        return end

evaluate_test_cases(quick_sort , tests)


'''
Time Complexity of Quicksort

If we partition the list into two nearly equal parts,then the complexity analysis is similar to that of merge sort and quicksort has the complexity  𝑂(𝑛log𝑛) . 
This is called the average-case complexity.


Worst case partitioning:

In this case, the partition is called n times with lists of sizes n, n-1... 
so that total comparisions are  𝑛+(𝑛−1)+(𝑛−2)+...+2+1=𝑛∗(𝑛−1)/2 . So the worst-case complexity of quicksort is  𝑂(𝑛2) .


Space Complexity of Quicksort

if we want to include space that we need initiali to store input that its O(N) but additional space is O(1)
'''
