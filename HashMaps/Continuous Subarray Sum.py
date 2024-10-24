"""
1. Prefix sum figured out
2. Two sum logic also figured out

"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        [23,2,4,6,7]
        [0,23,25,29,35,42]
        
        [0]
        [0,0]


        (j - i)%k == 0

        i%k = j%k
        """

        if len(nums)+1 > 2*k:
            return True

        prev_rem = {0:0}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum%k in prev_rem:
                if i+1 - prev_rem[curr_sum%k] > 1:
                    return True
            else:
                prev_rem[curr_sum%k] = i+1

        return False

"""
[5,0,0,0]
len(nums) + 1 > k

prev_rem {
    0:0
    2:1
}

curr_sum=5


[1,0,1,0,1]
[0,1,1,2,2,3]
"""