"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

1. For getting the next permutation, we need to increase the number as little as possible.
2. We need to find the first number from the end that is not in increasing order.
3. We need to find the number that is just greater than that number on the right side.
4. Swap the two numbers.
5. Reverse the numbers from the next index of the first number that we found, to set the numbers in increasing order.
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        x_i = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                x_i = i
                break

        if x_i == len(nums)-1:
            nums[:] = nums[::-1] 
            return
        else:
            y_i = x_i + 1
            while y_i < len(nums) and nums[y_i] > nums[x_i]:
                y_i+=1
            y_i-=1

            nums[x_i], nums[y_i] = nums[y_i], nums[x_i]
            nums[x_i+1:] = nums[-1:x_i:-1]