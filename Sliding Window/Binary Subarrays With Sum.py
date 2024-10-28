class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        """
        1. Presence of 0s complicate the sliding window technique in this example
        2. An interesting approach here that could have been used was that do the normal sliding window and count all the subsets that are <= target. 
        3. subsets with <=target - subsets with <= target-
        
        Structure is kinda clear:
        1. Incrementing the right pointer through a loop
        2. Inculcating the right pointer data
        3. Logic to shift the left pointer
        4. Validity check after shifting the left pointer
        """
        l = 0
        curr_sum = 0
        ans = 0
        prefix_zeroes=0

        # Incrementing the right pointer
        for r in range(len(nums)):

            # Inculcating the right pointers data
            curr_sum += nums[r]

            # Logic to shift the left pointer
            # 1. l should be less than r
            # 2. shifting condition
            while l < r and (nums[l] == 0 or curr_sum > goal):
                if nums[l] == 1:
                    prefix_zeroes = 0
                else:
                    prefix_zeroes+=1

                curr_sum -= nums[l]
                l+=1
            
            # Checking the validity
            if curr_sum == goal:
                ans+=1+prefix_zeroes

        return ans

"""
[1,0,1,0,1]

l=1
r=4
goal=1
ans=2

"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        """
        1. Presence of 0s complicate the sliding window technique in this example
        """
        

        def subsets_with_sum_lte_goal(val):
            nonlocal nums

            if val < 0:
                return 0

            ans = 0
            l = 0
            win_sum = 0

            for r,r_val in enumerate(nums):
                win_sum+=r_val

                while l<=r and win_sum > val:
                    win_sum-=nums[l]
                    l+=1

                print(r-l+1)
                ans += r - l + 1

            return ans
        
        return subsets_with_sum_lte_goal(goal) - subsets_with_sum_lte_goal(goal-1)

"""
[1,0,1,0,1]

l=0
win_sum = 2
r=1

ans = 1+2 + 
"""