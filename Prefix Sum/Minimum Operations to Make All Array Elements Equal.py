from bisect import bisect_left,bisect_right
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        nums = sorted(nums)
        pfx_sum = [0]*(len(nums)+1)

        for i in range(len(nums)):
            pfx_sum[i+1] = pfx_sum[i] + nums[i]

        ans = []

        for target in queries:
            #Find the increment
            ops = 0

            i = bisect_left(nums,target)
            ops += target*i - pfx_sum[i]

            #Find the decrements
            i = bisect_right(nums,target)
            ops += pfx_sum[-1] - pfx_sum[i] - target*(len(nums)-i)

            ans.append(ops)

        return ans



"""
nlogn
nums =      1,3,6,8

n
pfx_sum =   0,1,4,10,18


"""