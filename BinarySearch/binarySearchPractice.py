from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. 
rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
'''

# ---------------------------------------------------------------------------------------------------------------------------

'''
Solution


1. State the problem clearly. Identify the input & output formats

While this problem is stated clearly enough, it's always useful to try and express in your own words, 
in a way that makes it most clear for you. 
It's perfectly OK if your description overlaps with the original problem statement to a large extent.


Q: Express the problem in your own words below
Problem
Givan a rotated sorted list that was rotated some unknown number of times, we need to find num of times it is rotated.


Q: The function you write will take one input called nums. What does it represent? Give an example.
Input
A sorted rotated list e.g. [ 7, 9 ,3, 5, 6]


Q: The function you write will return a single output called rotations. What does it represent? Give an example.
Output
The numbers of times the sorted list was rotated e.g. 2times

#---------------------------------------------------------------------------------------------------------------------------------------

2. Come up with some example inputs & outputs. Try to cover all edge cases.
Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:

A list of size 10 rotated 3 times.
A list of size 8 rotated 5 times.
A list that wasn't rotated at all.
A list that was rotated just once.
A list that was rotated n-1 times, where n is the size of the list.
A list that was rotated n times (do you get back the original list here?)
An empty list.
A list containing just one element.
'''
test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

# A list of size 8 rotated 5 times.
test0 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

# A list that wasn't rotated at all.
test1 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    'output': 0
}

# A list that was rotated just once.
test2 = {
    'input': {
        'nums': [7, 3, 5]
    },
    'output': 1
}


# A list that was rotated n times where n is size of the list
test4 = {
    'input': {
        'nums': [3, 5, 7, 9, 10]
    },
    'output': 0
}


# A list is empty
test5 = {
    'input': {
        'nums': []
    },
    'output': 0
}


# A list contains only one element
test6 = {
    'input': {
        'nums': [5]
    },
    'output': 0
}

tests = [test, test0, test1, test2, test4, test5, test6]


#---------------------------------------------------------------------------------------------------------------------------------------


'''
3. Come up with a correct solution for the problem. State it in plain English.


Our first goal should always be to come up with a correct solution to the problem, 
which may not necessarily be the most efficient solution. Try to think of a solution before you read further.

Coming up with the correct solution is quite easy, and it's based on this insight: 
If a list of sorted numbers is rotated k times, then the smallest number in the list ends up at position k (counting from 0).
Further, it is the only number in the list which is smaller than the number before it. 
Thus, we simply need to check for each number in the list whether it is smaller than the number that comes before it (if there is a number before it). 
Then, our answer i.e. the number of rotations is simply the position of this number is . 
If we cannot find such a number, then the list wasn't rotated at all.

Example: In the list [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], the number 3 is the only number smaller than its predecessor. 
It occurs at the position 3 (counting from 0), hence the array was rotated 3 times.


That will be done with implementation of linear Search Algrotithm.
Here are steps:
1. create var position with value 0
2. loop through nums and compare each one with number before
3. if the number is smaller return position as result
4. otherwise increment position
5. if there is no number return 0


def count_rotations(nums):
    position = 0                  # Initial value of position

    while position < len(nums):     # when should we loop

         # Success criteria: check whether the number at the current position is smaller than the one before it  
        if position > 0 and nums[position] < nums[position - 1]:    # How to perform the check?
            return position
        position += 1
    return 0                                                        # What if none of the positions passed the check
'''

'''
4. Apply the right technique to overcome the inefficiency. Repeat steps 3 and 4.

As you might have guessed, we can apply Binary Search to solve this problem. 
The key question we need to answer in binary search is:
 Given the middle element, how to decide if it is the answer (smallest number), or whether the answer lies to the left or right of it.

If the middle element is smaller than its predecessor, then it is the answer.
However, if it isn't, this check is not sufficient to determine whether the answer lies to the left or the right of it.
Consider the following examples.

[7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)

[1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

Here's a check that will help us determine if the answer lies to the left or the right:
If the middle element of the list is smaller than the last element of the range, then the answer lies to the left of it.
Otherwise, the answer lies to the right.
'''


def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return 0

def count_rotations(nums):
    def condition(mid):
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return 'found'
            elif nums[mid] < nums[len(nums) - 1]:
                return 'left'
            else:
                return 'right'
    return binary_search( 0, len(nums)-1 , condition)


extended_tests = list(tests)


extended_tests.append({
    'input' : {
        'nums' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]
    },
    'output' : 16
})


'''
class Solution(object):
    def binary_search_leetcode(self,first, last, condition):
        while first <= last:
            mid = (first + last) // 2
            result = condition(mid)
            if result == 'found':
                return mid
            elif result == 'left':
                last = mid - 1
            else:
                first = mid + 1
        return -1 


    def search(self,nums, target):
        first = 0
        last = len(nums) - 1
        
        def condition(mid):
            if nums[mid] == target:
                return 'found'
            
            #When mid is smaller than first
            if nums[mid] < nums[first]:         # [5, 6, 9, 0, 2, 3, 4], [5,6,0,1,2,3,4]
                if nums[mid] < nums[mid-1]:     # middle is the smallest [5, 6, 9, 0, 2, 3, 4]
                    if target >= nums[first]:   # target 5,6,9
                        return 'left'
                    else:                       # target 2,3,4
                        return 'right'
                else:                           # [5,6,0,1,2,3,4]
                    if target >= nums[first] or target < nums[mid]:   # target 5,6,0
                        return 'left'
                    elif target > nums[mid] and target < nums[first]: # target 2,3,4
                        return 'right'
                    
            #When mid is greater than first
            else:                               # [4,5,6,7,0,1,2], [4,5,6,7,8,9,0,1,2]
                if target < nums[mid] and target >= nums[first]: #target 4,5,6 and 4,5,6,7
                    return 'left'
                elif target > nums[mid] or target < nums[first]: #target 9 and 0,1,2
                    return 'right'
        
        return self.binary_search_leetcode(first, last, condition)
'''

    

evaluate_test_cases(count_rotations, extended_tests)