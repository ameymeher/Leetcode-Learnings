from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        reservoir_size = 0
        ans = -1
        for i,num in enumerate(self.w):
            reservoir_size+=num
            if (randint(1,reservoir_size) > reservoir_size-num):
                ans = i
        return ans
    
"""
1,3,7
selecting 0: (1/1) * (1/4) * (4/11) = 1/11
selecting 1: (3/4) * (4/11)         = 3/11
selecting 2: (7/11)                 = 7/11
"""