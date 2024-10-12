"""
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        Assumptions:
        1. array of intervals, with start and end
        2. Inclusive
        3. Divide it in groups
        4. No intersecting intervals in one group
        5. left <= right
        6. array is not sorted

        Edge cases:
        1. 1 interval atleast


        [[5,10],[6,8],[1,5],[2,3],[1,10]]

        [[1,5],[1,10],[2,3],[5,10],[6,8],[12,15]]

        [1,5],[6,8]
        [1,10]
        [2,3],[5,10]

        15

        ans = 3
        """
        from heapq import heappush, heappop

        end_heap = []

        intervals.sort() #O(NlogN)

        for (start,end) in intervals: #O(N)

            # Add it to the existing group
            if end_heap and end_heap[0] < start: # O(N)
                heappop(end_heap) #O(1)

            # Create a new group
            heappush(end_heap,end) #O(logk)
            
        return len(end_heap)

"""
Time complexity : O(NlogN)
Space complexity: O(N)
"""