'''
Reverse bits of a given 32 bits unsigned integer.

'''

def reverse_bits(n):
    res = 0
    for i in range(32):
        bit = ( n >> i ) & 1
        res = res | (bit << 31 - i)
    return res