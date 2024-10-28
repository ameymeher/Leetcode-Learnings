"""
1. A stack solution is also good, just store -1 at the start and calculate the max_length for each pop
2. left and right counts can be maintained, but need to do this in two passes like the below
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlength = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left > right:
                left = right = 0
                
        return maxlength