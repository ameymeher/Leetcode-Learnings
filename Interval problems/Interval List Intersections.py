"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

1. For checking the intersection:
    a. The start of the second interval should be less than the end of the first interval.
    b. The end of the second interval should be greater than the start of the first interval.
"""

class RangeElement:
    def __init__(self,val):
        self.start = val[0]
        self.end = val[1]

    def __lt__(self,other):
        return self.end < other.end

    def has_intersection(self,other):
        if self.end >= other.start and self.start <= other.end:
            return True
        return False

    def intersection(self,other):
        if self.has_intersection(other):
            return (max(self.start,other.start),min(self.end,other.end))
        return None

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        from collections import deque

        i,j = 0,0

        ans = []

        firstList = list(map(RangeElement,firstList))
        secondList = list(map(RangeElement,secondList))

        while i<len(firstList) and j<len(secondList):
            if firstList[i].has_intersection(secondList[j]):
                ans.append(firstList[i].intersection(secondList[j]))

            if firstList[i] < secondList[j]:
                i+=1
            else:
                j+=1

        return ans