class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Assumptions:
        1. Update the numbers in place
        2. Remove by updating the number by _
        3. All are int

        """

        if not nums:
            return 0

        l = 0
        r = len(nums)-1

        while l<r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r],nums[l]
                r-=1
            else:
                l+=1

        return l if nums[l] == val else l+1

"""
[0,1,4,0,3,2,2,2] 2

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Assumptions:
        1. Update the numbers in place
        2. Remove by updating the number by _
        3. All are int

        """

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        
        return k

"""
[0,1,4,0,3,2,2,2] 2

"""
[]