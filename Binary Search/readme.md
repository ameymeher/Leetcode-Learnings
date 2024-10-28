# Binary Search Tips

1. mid = (left + right)//2 gives the left middle element.
2. mid = (left + right + 1)//2 gives the right middle element.
3. For bisect_left, use mid = (left + right)//2. For the equal case, move right to mid.
4. For bisect_right, use mid = (left + right + 1)//2. For the equal case, move left to mid.


5. Binary search can be used to find the starting of a range as well. Just a change in the logic is required. Example [Find K Closest Elements](./Find%20K%20Closest%20Elements.py)


6. mid with some value comparison which we are finding is the key to converge the search space.
7. l and r must be some valid boundaries. They can be min and max values, or min and max indexes
8. The shifting condition should be linked directly to the values of the array. It can be anything, starting of a range, finding the kth smallest element, finding the value etc. Example [kth Smallest Element in a Sorted Matrix](./Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix.py)
9. It always converges to the index or the value which we are finding. 


10. Binary search on the answer range
11. Patterns to notice - the answer can be checked and verified in O(N) or less time. Its a sign to use this pattern
12. The range of the answer is known, like the minimum and the maximum is known. Thus we can use a range
12. Take care of the True and False in the array.