class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        1. Lists are sorted
        2. Need to find the smallest range covering ATLEAST one number from each of the k lists

        [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

        min_heap = [(4,0),(5,2),(9,1)] 
        k = 3
        iterators = [1,2,1]
        curr_end = 9
        ans = (0,5)

        """
        from heapq import heappush,heappop
        
        min_heap = []
        k = len(nums)

        def get_iterator(arr):
            yield from arr

        iterators = [get_iterator(arr) for arr in nums]

        curr_end = -float('inf')
        ans = (-float('inf'),float('inf'))

        while True:
            if len(min_heap) < k:
                val = (next(iterators[len(min_heap)],None),len(min_heap))
                heappush(min_heap,val)
                curr_end = max(curr_end,val[0])
            else:

                ans = min(ans,(min_heap[0][0],curr_end),
                        key = lambda x: (x[1]-x[0],x[0]))

                _,i = heappop(min_heap)
                val = next(iterators[i],None)

                if val is None:
                    return ans

                curr_end = max(curr_end,val)
                heappush(min_heap,(val,i))