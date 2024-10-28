"""
In this question, we were challenged with maintaining the order of the window
Insertion and deletion was required to be faster, thus used Self balancing binary search trees with log(k) times

A crazy solution was not to maintain the sorting, but have buckets in which the elements would be kept.
Get the bucket of the current element and just check one previous and next bucket if the value is there.
Buckets are crazy good and a way to spot this is when we have a range defined
"""

# Solution 1: Using Self balancing BST O(Nlogk)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList

        window = SortedList()
        l = 0

        # increment the value of r
        for r in range(len(nums)):

            # Updating the answer
            i = window.bisect_left(nums[r])
            if ((i!= len(window) and abs(window[i] - nums[r]) <= valueDiff) or
                (i-1>= 0 and abs(window[i-1] - nums[r]) <= valueDiff)):
                return True

            # Inculcate the value of r, don't have to do that here
            window.add(nums[r])

            # Slide the l pointer
            while l<=r and r-l >= indexDiff:
                window.remove(nums[l])
                l+=1
            
        return False

# Solution 2: Using buckets O(N) solution

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        buckets = {}

        for i,num in enumerate(nums):
            bucket = num // (valueDiff+1)

            if bucket in buckets:
                return True

            if bucket-1 in buckets and abs(buckets[bucket-1] - num) <= valueDiff:
                return True

            if bucket+1 in buckets and abs(buckets[bucket+1] - num) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >=indexDiff:
                del buckets[nums[i-indexDiff]//(valueDiff+1)]

        return False