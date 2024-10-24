"""
1. Learned how to use key in min function


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Assumptions:
        1. Can the tree be null? No
        2. There can be negative values as well right

        Edge case:
        One node
        """

        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right

        return closest


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Assumptions:
        1. Can the tree be null? No
        2. There can be negative values as well right

        Edge case:
        One node
        """

        diff = float('inf')
        ans = float('inf')

        while root:
            
            if abs(root.val - target) < diff:
                ans = root.val
                diff = abs(root.val - target)
            elif abs(root.val - target) == diff:
                ans = min(ans,root.val)

            if root.val >= target:
                root = root.left
            else:
                root = root.right

        return ans