"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

1. For checking the intersection:
    a. The start of the second interval should be less than the end of the first interval.
    b. The end of the second interval should be greater than the start of the first interval.
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        ans = []

        first = 0
        second = 0

        def has_intersection(i1,i2):
            return i1[1] >= i2[0] and i2[1] >= i1[0]

        while first < len(firstList) and second < len(secondList):
            
            i1, i2 = firstList[first], secondList[second]

            # For intersection answer
            # if i1[1] >= i2[0] and i2[1] >= i1[0]:
            #     ans.append([max(i1[0],i2[0]),min(i1[1],i2[1])])

            # For union answer
            if has_intersection(i1,i2):
                new_i = [min(i1[0],i2[0]),max(i1[1],i2[1])]

                if not ans or not(ans[-1][1] >= new_i[0] and new_i[1] >= ans[-1][0]):
                    ans.append([min(i1[0],i2[0]),max(i1[1],i2[1])])
                else:
                    prev_i = ans.pop()
                    ans.append([min(prev_i[0],new_i[0]),max(prev_i[1],new_i[1])])

            if i1[1] > i2[1]:
                second+=1
            elif i1[1] < i2[1]:
                first += 1
            else:
                first+=1
                second+=1


        while first < len(firstList):
            i = firstList[first]
            if ans and has_intersection(ans[-1],i):
                prev_i = ans.pop()
                ans.append([min(prev_i[0],i[0]),max(prev_i[1],i[1])])
            else:
                ans.append(firstList[first])
            first+=1

        while second < len(secondList):
            i = secondList[second]
            if ans and has_intersection(ans[-1],i):
                prev_i = ans.pop()
                ans.append([min(prev_i[0],i[0]),max(prev_i[1],i[1])])
            else:
                ans.append(secondList[second])
            second+=1

        return ans

"""

[0,12],[13,26]

"""