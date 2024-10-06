"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        max_h = -1

        def traverse(root,h):
            nonlocal max_h, ans

            if not root:
                return

            if h > max_h:
                max_h = h
                ans.append(root.val)

            traverse(root.right,h+1)
            traverse(root.left,h+1)

        def iterative_traversal(root):
            nonlocal max_h, ans

            stack = [(root,0)]

            while stack:
                node,h = stack.pop()
                if node:
                    if h > max_h:
                        max_h = h
                        ans.append(node.val)
                    
                    stack.append((node.left,h+1))
                    stack.append((node.right,h+1))

        #traverse(root,0)
        iterative_traversal(root)

        return ans