"""
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).

1. n-1 flips the least signigicant bit that is 1 to 0 and all the bits to the right of it to 1.
2. n & n-1 removes the least significant bit that is 1.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count+=1
            n&=n-1
        return count