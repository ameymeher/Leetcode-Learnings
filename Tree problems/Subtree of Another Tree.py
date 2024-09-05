"""
1. Can be solved using the prefix traversal string of both trees
2. Just check if the string of the subtree is present in the string of the main tree
3. Better than checking each node of the subtree in the main tree, over and over again
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Best solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"

        return convert(subRoot) in convert(root)
    
#Alternate solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):
            if (p and not q) or (not p and q):
                return False

            if p and q:
                #print(f"Checking {p.val} and {q.val}")
                if p.val != q.val:
                    return False
                
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            else:
                return True

        queue = [root]

        for node in queue:
            if not node:
                if isSameTree(node,subRoot):
                    return True
                continue
            
            if node.val == subRoot.val:
                if isSameTree(node,subRoot):
                    return True
            print("heher")
            queue.append(node.left)
            queue.append(node.right)
            print(len(queue))

        return False