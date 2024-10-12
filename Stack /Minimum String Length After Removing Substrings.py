"""
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

 

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
Example 2:

Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.

1. Used the stack perfectly to solve the problem.
"""

class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []

        for c in s:
            if stack and ((c == 'B' and stack[-1] == 'A') or (c=='D' and stack[-1] == 'C')):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)