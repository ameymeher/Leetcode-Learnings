"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

1. What I was thinking was doing two loops, outer one to figure out the first digit, inner to figure out the highest digit.
2. If there was a swap, then do it and return the number
3. I came across this crazy logic that can do it in O(N) time.
4. We have to find the highest number from the back, we can do it in a O(N) time.
5. At the same time, we have to find the digit which is lesser than the CURRENT highest digit.
6. We can do it in the same loop. This is a greedy approach.
"""

# O(N^2) solution that I implemented
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        for i in range(0,len(num)-1):
            max_swap = num[i]
            max_swap_index = i

            for j in range(i+1,len(num)):
                if num[j] >= max_swap:
                    max_swap = num[j]
                    max_swap_index = j
                    
            if num[max_swap_index] != num[i]:
                num[i],num[max_swap_index] = num[max_swap_index], num[i]
                break

        return int(''.join(num))
    
# The crazy O(N) solution that I came across and 
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        max_i = len(num)-1
        small,large = 0,0

        for i in range(len(num)-1,-1,-1):
            if num[i] > num[max_i]:
                max_i = i
            elif num[i] < num[max_i]:
                small = i
                large = max_i

        num[small],num[large] = num[large],num[small]
        return int(''.join(num))