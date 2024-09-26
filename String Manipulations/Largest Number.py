"""
1. Learned how to sort on a custom condition
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        class Larger(str):
            def __lt__(x,y):
                return x+y > y+x

        nums = list(map(Larger,nums))
        nums = sorted(nums,key=Larger)

        for i in range(len(nums)):
            if nums[i] != '0':
                break
            if nums[i] == '0' and i!=len(nums)-1:
                nums[i]=''
            
        return ''.join(nums)