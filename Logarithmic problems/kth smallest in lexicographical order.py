"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr: int, n: int) -> int:
            steps = 0
            first = curr
            last = curr + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps

        curr = 1
        k -= 1  

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  
            else:
                curr *= 10  
                k -= 1  

        return curr