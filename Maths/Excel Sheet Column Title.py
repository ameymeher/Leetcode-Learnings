"""
1. Crazy thing here was the numbers started from 1 and not zero
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber-=1
            ans = chr((columnNumber)%26 + ord('A')) + ans
            columnNumber//=26
        return ans

"""
14655
26
"""
