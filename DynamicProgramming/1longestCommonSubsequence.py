from re import A
from tkinter import N
from jovian.pythondsa import evaluate_test_cases
'''
Longest Common Subsequence

QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences. 
E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. 
For example, "edpt" is a subsequence of "serendipitous".
'''

'''
Test cases:
    General case (string)
    General case (list)
    No common subsequence
    One is a subsequence of the other
    One sequence is empty
    Both sequences are empty
    Multiple subsequences with same length
        “abcdef” and “badcfe”
'''

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T2 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]


'''
BRUTE FORCE SOLUTION

Recursive Solution

Create two counters idx1 and idx2 starting at 0. Our recursive function will compute the LCS of seq1[idx1:] and seq2[idx2:]

If seq1[idx1] and seq2[idx2] are equal, then this character belongs to the LCS of seq1[idx1:] and seq2[idx2:] (why?). 
Further the length this is LCS is one more than LCS of seq1[idx1+1:] and seq2[idx2+1:]

If not, then the LCS of seq1[idx1:] and seq2[idx2:] is the longer one among the LCS of seq1[idx1+1:], seq2[idx2:] and the LCS of seq1[idx1:], seq2[idx2+1:]

If either seq1[idx1:] or seq2[idx2:] is empty, then their LCS is empty.
'''

def lcs_recursive(seq1 , seq2 , idx1=0 , idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1 , seq2 , idx1 + 1 , idx2 + 1)
    else:
        option1 = lcs_recursive(seq1 , seq2 , idx1 + 1 , idx2)
        option2 = lcs_recursive(seq1 , seq2 , idx1 , idx2 + 1)
        return max(option1 , option2)

#evaluate_test_cases(lcs_recursive , lcq_tests)

