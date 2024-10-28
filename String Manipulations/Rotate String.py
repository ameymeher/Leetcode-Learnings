"""
1. slicing operator takes O(n) time
2. Comparing a deque object takes O(n) time
3. If a rotation is to be seen, append the original to itself and check if the goal is there or not
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s+s)
