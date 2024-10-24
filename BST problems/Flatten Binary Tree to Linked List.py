# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. Think about postorder when changing the structure of the tree
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def post_order(root): #head and the tail return
            if not root:
                return None

            left_tail = post_order(root.left)
            right_tail = post_order(root.right)

            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            return right_tail or left_tail or root

        root = post_order(root)

        return root