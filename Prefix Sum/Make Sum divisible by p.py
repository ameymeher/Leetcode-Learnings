"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

1. Crazy problem. Use prefix sum
2. Obviosly, need to find a subarray that (pfx[j] - pfx[i])%p == total_sum%p. Then we can remove this subarray.
3. A normal way to do this is to use 2 loops, but that will go for O(n^2).
4. We shift the equation to (pfx[j]-total_sum)%p == pfx[i]%p. 
5. We did this because we have pfx[j] and total_sum in the iteration.
6. We can store the pfx[i]%p in a hashmap, so we don't need to iterate again, since i was seen earlier.
7. We need to handle the case where the whole array is the answer, so we need to initialize the hashmap with {0:-1}.
8. This was the second time I saw this pattern. Crazy stuff. After seeing the equation, it becomes very easy.
"""

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        
        if total%p == 0:
            return 0

        target = total%p

        curr_sum = 0
        i_map = {0:-1}
        ans = float('inf')

        for j,j_val in enumerate(nums):
            curr_sum += j_val

            """
            Equation is:
            (pfx_j - pfx_i)%p = target%p
            (pfx_j - target + p)%p = pfx_i
            """

            i_val = (curr_sum - target + p)%p

            if i_val in i_map:
                ans = min(ans,j-i_map[i_val])
            
            i_map[curr_sum%p] = j

        return -1 if ans ==len(nums) else ans