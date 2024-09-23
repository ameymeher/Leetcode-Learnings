"""
You are given a 0-indexed string s and a dictionary of words dictionary. 
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.
"""

from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)

        @cache
        def dp(start):
            nonlocal s

            if start == len(s):
                return 0

            ans = dp(start+1)+1

            for i in range(start,len(s)):
                if s[start:i+1] in dictionary:
                    ans = min(ans,dp(i+1))

            return ans
        
        return dp(0)