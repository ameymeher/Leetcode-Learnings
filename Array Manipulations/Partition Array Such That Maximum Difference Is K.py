class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        from bisect import bisect_right

        if k == 0:
            return len(set(nums))

        nums.sort()
        l = 0
        ans = 0
        while l<len(nums):
            l += bisect_right(nums[l:],nums[l]+k)
            ans+=1

        return ans


"""
1,2,3,5,6
"""
