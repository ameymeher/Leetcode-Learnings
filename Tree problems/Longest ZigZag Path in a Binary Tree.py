"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

1. Instead of returning the max value, I should have used a global variable to store the max value.
2. It was very easy as can be seen from the code.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def get_max(root,left,steps):
            nonlocal ans

            if not root:
                return 

            ans = max(ans,steps)

            if left:
                get_max(root.left,False,steps+1)
                get_max(root.right,True,1)
            else:
                get_max(root.right,True,steps+1)
                get_max(root.left,False,1)

        get_max(root,True,0)
        get_max(root,False,0)

        return ans
