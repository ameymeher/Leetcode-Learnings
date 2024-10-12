"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

"""

# O(N^2) solution - Brute force

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        ans = 0

        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i] <= nums[j]:
                    ans = max(ans,j-i)

        return ans
    
# O(NlogN) solution
"""
1. Just keep a track of the minimum index so far.
2. If the current index is greater than the minimum index, then update the answer.
3. Else update the minimum index.
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        nums = sorted(list(enumerate(nums)),key=lambda x: (x[1],x[0]))

        min_index = len(nums)-1
        ans = 0

        for i,_ in nums:
            if i < min_index:
                min_index = i
            else:
                ans = max(ans,i-min_index)
    
        return ans