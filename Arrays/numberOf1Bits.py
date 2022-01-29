'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''

def hammingWeight(self, n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res
        

            