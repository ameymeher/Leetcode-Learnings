"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

1. For palindrome questions, try thinking coming inwards from the ends or reaching outwards from center.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_substring(i,j):
            nonlocal s

            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        i = 0
        j = len(s)-1

        while i < j:
            if s[i] != s[j]:
                return check_substring(i+1,j) or check_substring(i,j-1)
            i+=1
            j-=1

        return True


