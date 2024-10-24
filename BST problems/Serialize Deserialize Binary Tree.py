# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ans = '' # '1,2,None,None,3,4,None,None,5,'
        def preorder(root):
            nonlocal ans
            if not root:
                ans += 'None,'
                return
            ans+=str(root.val)+','
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans[:-1] #'1,2,None,None,3,4,None,None,5,None,None'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        
        vals = deque(data.split(',')) #'[1,2,None,None,3,4,None,None,5,None,None]'

        def build_tree_preorder():
            nonlocal vals

            val = vals.popleft()
            if val == 'None':
                return None

            node = TreeNode(val)
            node.left = build_tree_preorder()
            node.right = build_tree_preorder()

            return node

        root = build_tree_preorder()

        return root
            
"""
1
L 2
    L None
    R None
R 3
    L 4
        L None
        R None
    R 5
        L None
        R None
"""


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))