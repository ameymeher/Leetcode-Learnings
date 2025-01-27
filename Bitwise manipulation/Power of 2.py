"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        1. An integer is given
        2. 1,2,4 - All should return True

        Bit wise manipulation
        """
        return n and not(n&n-1)