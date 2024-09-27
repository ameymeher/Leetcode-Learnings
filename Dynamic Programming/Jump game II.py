"""
1. Learned the concept of applying greedy approach here
2. The idea is to keep track of the current farthest point we can reach from the current point
3. When the current point reaches the end, we update the current end to the current farthest point
4. We increment the answer by 1
5. Time complexity: O(n)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ans = 0
        curr_end = 0
        curr_far = 0

        for i in range(len(nums)-1):
            curr_far = max(curr_far,i+nums[i])
            if i==curr_end:
                ans+=1
                curr_end = curr_far
        
        return ans
            
