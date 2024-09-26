"""
Start from the back and keep a track till where we have reached till now
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0