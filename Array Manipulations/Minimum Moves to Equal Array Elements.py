class Solution:
    def minMoves(self, nums: List[int]) -> int:

        ans = 0
        min_value = float('inf')

        for num in nums:
            ans+=num
            min_value = min(num,min_value)

        return ans - min_value*len(nums)