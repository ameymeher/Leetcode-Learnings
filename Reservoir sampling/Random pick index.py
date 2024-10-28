from random import randint

class Solution:

    def __init__(self,arr):
        self.arr = arr

    def pick_index(self,target):

        count = 0
        ans = -1
        for i,num in enumerate(self.arr):
            if num == target:
                count += 1
                if randint(1,count) == count:
                    ans = i
        
        return ans
    
"""
1,2,3,3,3,3

selecting index 2: (1/1) * (1/2) * (2/3) * (3/4) = 1/4
selecting index 3: (1/2) * (2/3) * (3/4) = 1/4
selecting index 4: (1/3) * (3/4) = 1/4

1. Keep increasing the reservoir
2. Get the index if the random number == reservoir size
selecting index i: (i/i) * (i/i+1) * (i+1/i+2)...(n-1/n) = 1/n
"""