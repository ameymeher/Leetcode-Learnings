"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def calc_max_h(root):
            nonlocal ans

            if not root:
                return 0

            if not root.left and not root.right:
                return 0
            
            left_h, right_h = 0,0

            if root.left:
                left_h = calc_max_h(root.left)+1

            if root.right:
                right_h = calc_max_h(root.right)+1

            ans = max(ans,left_h + right_h)

            return max(left_h,right_h)

        calc_max_h(root)

        return ans