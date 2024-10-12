"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Assumptions:
        1. BST
        2. left - predecessor
        3. right - successor
        4. Return the pointer of the smallest element in the LL
        5. Looks like an inorder traversal
        6. Need to create a link in place

        Edge cases:
        1. One node -  circular to itself and return
        2. No node - return null

        head = 1
        pre = 4
        suc

        """

        prev = None
        first = None

        def inorder(root): #O(N) solution
            nonlocal prev,first

            if not root:
                return

            inorder(root.left)

            if prev:
                prev.right = root
                root.left = prev
            else:
                first = root

            prev = root

            inorder(root.right)

        if not root:
            return None

        inorder(root)

        prev.right = first
        first.left = prev

        return first
    
"""
Time complexity: O(N) for going through all the nodes
Space complexity: O(N) for maintaining the recursion stack
"""