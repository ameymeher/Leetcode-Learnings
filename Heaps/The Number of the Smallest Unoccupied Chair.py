"""
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

1. Please use heappop!
2. 
"""
from heapq import heappush,heappop
from collections import defaultdict

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        

        """
        Assumptions:
        1. times array is not sorted
        2. start is inclusive and end is not inclusive
        3. i < n
        4. 0 indexed chairs
        5. ith targetFriend in the unsorted order we have to find
        6. arrival time starts from the first friend
        """

        times = sorted(list(enumerate(map(tuple,times))),key = lambda x: x[1])

        curr_chair = 0
        min_chairs = []
        min_end = []
        end_chair_map = defaultdict(list)

        for i,(start,end) in times:

            # Free up the chairs till that time
            while min_end and start >= min_end[0]:
                end_done = heappop(min_end)
                for chair in end_chair_map[end_done]:
                    heappush(min_chairs,chair)
                del end_chair_map[end_done]

            # If there are freed chairs
            if min_chairs:
                chair = heappop(min_chairs)
            else:
                chair = curr_chair
                curr_chair+=1

            # Assign this chair till this end time and append the min end too
            if end not in end_chair_map:
                heappush(min_end,end)
            end_chair_map[end].append(chair)

            if i==targetFriend:
                return chair

"""
times = [(1,2),(1,2),(2,3),(3,4)]

curr_time = 3
curr_chair = 2
min_chairs = [0,1]
min_end = [4]
end_chair_map = {4:0}
chair = 1
"""