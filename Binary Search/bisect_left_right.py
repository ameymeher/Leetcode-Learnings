"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

1. Don't forget to check the edge case of empty array
2. Main edge case is when the array has two same elements, handle this and the problem is done
3. For the left one, keep the left mid for even cases
4. For the right one, keep the right mid for even cases
5. For the equal case, take the mid on the left side for the left one
6. For the equal case, take the mid on the right side for the right one

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_left(val):
            nonlocal nums

            l = 0
            r = len(nums)-1

            print(l,r)

            while l<r:
                # For the left one, keep the left mid for even cases
                mid = (l+r)//2

                # For the equal case, take the mid on the left side
                if val <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            if nums and nums[l] == val:
                return l
            else:
                return -1

        def find_right(val):
            nonlocal nums

            l=0
            r=len(nums)-1

            while l<r:
                # For the right one, keep the right mid for even cases
                mid = (l+r+1)//2
                if val < nums[mid]:
                    r = mid-1

                # For the equal case, take the mid on the right side
                else:
                    l = mid

            if nums and nums[l] == val:
                return l
            return -1

        i = find_left(target)
        j = find_right(target)

        if i==-1:
            return (-1,-1)

        return(i,j)
        
"""
[5,7,7,8,8,10]

8
l=4
r=5
mid=4

1

"""
