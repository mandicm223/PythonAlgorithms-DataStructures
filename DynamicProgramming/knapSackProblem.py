
from jovian.pythondsa import evaluate_test_cases
'''
0-1 Knapsack Problem
Problem statement
You’re in charge of selecting a football (soccer) team from a large pool of players. 
Each player has a cost, and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. 
Assume that there’s no minimum or maximum team size.

General problem statemnt:

Given n elements, each of which has a weight and a profit, 
determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.
'''

'''
Test cases:

Some generic test cases
All the elements can be included
None of the elements can be included
Only one of the elements can be included
'''
test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests = [test0, test1, test2, test3, test4, test5]

'''
We'll write a recursive function that computes max_profit(weights[idx:], profits[idx:], capacity), with idx starting from 0.
If weights[idx] > capacity, the current element is cannot be selected, 
so the maximum profit is the same as max_profit(weights[idx+1:], profits[idx+1:], capacity).

Otherwise, there are two possibilities: we either pick weights[idx] or don't. We can recursively compute the maximum

    A. If we don't pick weights[idx], once again the maximum profit for this case is max_profit(weights[idx+1:], profits[idx+1:], capacity)

    B. If we pick weights[idx], the maximum profit for this case is profits[idx] + max_profit(weights[idx+1:], profits[idx+1:], capacity - weights[idx]

If weights[idx:] is empty, the maximum profit for this case is 0.
'''

def knapSackRecursive(weights , profits , capacity , idx= 0 ):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return knapSackRecursive(weights , profits , capacity , idx + 1)
    else:
        option1 = knapSackRecursive(weights , profits , capacity , idx + 1)
        option2 = profits[idx] + knapSackRecursive(weights , profits , capacity-weights[idx] , idx + 1)
        return max(option1 , option2)
    

#evaluate_test_cases(knapSackRecursive , tests)

def knapSackMemoized(weights , profits, capacity ):
    memo = {}
    def recurse( capacity , idx= 0):
        key = (capacity , idx)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > capacity:
            memo[key] = recurse(capacity , idx + 1)
        else:
            option1 = recurse(capacity , idx + 1)
            option2 = profits[idx] + recurse(capacity-weights[idx] , idx + 1)
            memo[key] = max(option1 , option2)
        return memo[key]
    return recurse(capacity) 

#evaluate_test_cases(knapSackMemoized , tests)

def knapSackDP(weights , profits , capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)]for _ in range(n+1)]
    for i in range(n):
        for c in range(1 , capacity + 1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c] , profits[i] + table[i][c - weights[i]])
    return table[-1][-1]

evaluate_test_cases(knapSackDP , tests)



