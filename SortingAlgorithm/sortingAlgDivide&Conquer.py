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


