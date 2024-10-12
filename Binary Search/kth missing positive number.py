"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

1. O(N) solution is also crazy.
2. O(log N) solution is after figuring the val - i-1 gives the number of missing numbers before that index.
3. Then, do a binary search to find the index where the missing number is.
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """ O(N) solution
        for num in arr:
            if num <= k:
                k += 1
            elif num > k:
                break
        return k
        """

        """ O(logN) solution"""

        from bisect import bisect_left
        
        def check(val_tup):
            nonlocal k
            i,val = val_tup
            if val-i-1 >= k:
                return True
            return False

        i = bisect_left(list(enumerate(arr)),True,key=check)

        return arr[i-1] + k - (arr[i-1] - i)

        """
        2 3 4 7 11, need to find 2nd missing number, 5th missing number, 3rd missing number
        1 2 3 4 5
        1 1 1 3 6
        """