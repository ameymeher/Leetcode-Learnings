class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        """
        limit=4
        8,12,4
        """

        """
        1. Maintaining the minimum and maximum in a specific ORDER by two queues
        2. If the current element is the global min or global max, we need that only. Pop all the elements till we reach this condition.
        3. For incrementing l, we need to see which were the min and max values entered previously.
        4. If those matches the left values, we need to remove them from the min or max queues.


        """
        from collections import deque

        min_queue = deque()
        max_queue = deque()
        max_length = 0
        l=0

        for r in range(len(nums)):

            # Inculcating the r value
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            min_queue.append(nums[r])

            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])

            # Adjusting the length of the window
            while l<=r and max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                l+=1

            # Answer update
            max_length = max(max_length,r-l+1)

        return max_length
    

"""
Approach 2: Using heaps
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        from heapq import heappush, heappop, heapify

        min_heap = []
        max_heap = []
        max_length = 0
        l=0

        for r in range(len(nums)):

            # Inculcating the r value
            heappush(max_heap,(-nums[r],r))
            heappush(min_heap,(nums[r],r))

            # Adjusting the length of the window
            while l<=r and (-max_heap[0][0] - min_heap[0][0]) > limit:
                l = min(max_heap[0][1],min_heap[0][1])+1

                while max_heap[0][1] < l:
                    heappop(max_heap)

                while min_heap[0][1] < l:
                    heappop(min_heap)

            # Answer update
            max_length = max(max_length,r-l+1)

        return max_length