# Binary Search Tips

1. mid = (left + right)//2 gives the left middle element.
2. mid = (left + right + 1)//2 gives the right middle element.
3. For bisect_left, use mid = (left + right)//2. For the equal case, move right to mid.
4. For bisect_right, use mid = (left + right + 1)//2. For the equal case, move left to mid.
5. Binary search can be used to find the starting of a range as well. Just a change in the logic is required. Example [Find K Closest Elements](./Find%20K%20Closest%20Elements.py)
