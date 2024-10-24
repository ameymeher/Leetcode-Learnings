class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left

        left = bisect_left(intervals,newInterval[0],key=lambda x: x[1])
        right = bisect_left(intervals,newInterval[1],key=lambda x: x[0])
        
        if right >= len(intervals) or intervals[right][0] > newInterval[1]:
            right-=1
        
        if left <= right:
            return intervals[:left] + [[min(intervals[left][0],newInterval[0]),max(intervals[right][1],newInterval[1])]] + intervals[right+1:]

        intervals.insert(left,newInterval)
        return intervals



"""
[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
left = 1
right = 3

[[1,3],[6,9]], newInterval = [2,5]
left = 0
right = 1
"""