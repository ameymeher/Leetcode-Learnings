"""
1. Best use case of recursion
2. Three cases:
    a. Node has no children
    b. Node has right child. Find the successor of the node and replace the node with the successor. Delete the successor node.
    c. Node has left child. Find the predecessor of the node and replace the node with the predecessor. Delete the predecessor node.
3. Time complexity: O(h) where h is the height of the tree

"""

class Solution:

    def successor(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self,root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right,root.val)
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left,root.val)
            else:
                root = None

        return root