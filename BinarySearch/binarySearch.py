from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


''' QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
 and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card. '''

# Basic test case

test = {
    'input' : {
        'cards' : [ 13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 7
    },

    'output' : 3
}

# All possible test cases
tests = []
tests.append(test)

 
# query is located at the beggining of the list
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})



# query is located at the end of the list

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# query is is the only number in the list

tests.append({
    'input' : {
        'cards' : [7],
        'query' : 7
    },

    'output' : 0
})

# query is part of the list

tests.append({
    'input' : {
        'cards' : [ 15, 12, 11, 10, 8],
        'query' : 7
    },

    'output' : -1
})

# other numbers in list are duplicating

tests.append({
    'input' : {
        'cards' : [ 8, 8, 8, 7, 6, 6, 5, 4, 3, 2],
        'query' : 7
    },

    'output' : 3
})

# query is duplicated

tests.append({
    'input' : {
        'cards' : [ 15, 12, 7, 11, 10, 7],
        'query' : 7
    },

    'output' : 2
})

# list of cards is empty

tests.append({
    'input' : {
        'cards' : [],
        'query' : 7
    },

    'output' : -1
})

''' Ineficient way
def locate_cards(cards, query):
    position = 0
    while len(cards) > position:
        if cards[position] == query:
            return position
        position += 1
    return -1
'''

# Implementing binary search
'''
1. Find the middle element of the list.
2. If it matches queried number, return the middle position as the answer.
3. If it is less than the queried number, then search the first half of the list
3. If it is greater than the queried number, then search the second half of the list
4. If no more elements remain, return -1.
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
    return -1


def locate_cards(cards,query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid -1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_search( 0, len(cards)-1 , condition)




evaluate_test_cases(locate_cards, tests)
