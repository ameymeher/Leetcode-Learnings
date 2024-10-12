"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

1. Keep a bal variable
    When adding to the left, increment bal
    When adding to the right, decrement bal
    When rebalancing, if moving from left to right, decrement bal by 2
    When rebalancing, if moving from right to left, increment bal by 2
    When lazy removing from the left, decrement bal
    When lazy removing from the right, increment bal
2. Use heappop and not pop, please!
3. make_top_ready is a function that removes the top elements from the heaps that are in the deletes dictionary
   Call this before using any of the tops for comparison
   Before adding, before removing, before getting the median

"""


from heapq import heappush, heappop, heapify
from collections import defaultdict

class MedianArray:

    def __init__(self,arr):
        self.l_max = []
        self.r_min = []
        self.bal = 0
        self.deletes = defaultdict(int)

        for val in arr:
            self.add(val)

    def rebalance(self):

        # Extra elements on the left side, Move to right
        while self.bal > 1:
            heappush(self.r_min,-heappop(self.l_max))
            self.bal-=2     # This was 2 dammit, not 1
        
        # Extra elements on the right side, Move to the left
        while self.bal < 0:
            heappush(self.l_max,-heappop(self.r_min))
            self.bal+=2


    def add(self,val):

        self.make_top_ready()

        # If there are no elements, append to left
        if not self.l_max:
            heappush(self.l_max,-val)
            self.bal += 1

        else:
            # Inserting on the left side
            if val < -self.l_max[0]:
                heappush(self.l_max,-val)
                self.bal += 1
                self.rebalance()
            # Inserting on the right side
            else:
                heappush(self.r_min,val)
                self.bal -=1
                self.rebalance()

    def lazy_remove(self,val):
        self.make_top_ready()

        self.deletes[val] += 1 # This should come after make_top_ready as it will delete it beforehand then

        # Remove from the left
        if val <= -self.l_max[0]:
            self.bal-=1

        # Remove from the right
        else:
            self.bal+=1

        self.rebalance()

    def make_top_ready(self):

        # Make the left top ready
        while self.l_max and -self.l_max[0] in self.deletes:
            val = -heappop(self.l_max) # Had to use heappop and not pop, dammit!
            self.deletes[val]-=1
            if self.deletes[val] == 0:
                del self.deletes[val]

        # Make the right top ready
        while self.r_min and self.r_min[0] in self.deletes:
            val = heappop(self.r_min)
            self.deletes[val]-=1
            if not self.deletes[val]:
                del self.deletes[val]

        self.rebalance()

    def get_median(self):
        self.make_top_ready()
        if self.bal == 0:
            return (-self.l_max[0] + self.r_min[0])/2
        return -self.l_max[0]
                
    def __repr__(self):
        return f'Left max Heap: {[-x for x in self.l_max]}\nRight min Heap: {self.r_min} Balance: {self.bal}\nDeletes: {self.deletes}\n'

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        window = MedianArray(nums[:k])
        ans = [window.get_median()]

        for i in range(k,len(nums)):
            window.lazy_remove(nums[i-k])
            window.add(nums[i])
            ans.append(window.get_median())

        return ans