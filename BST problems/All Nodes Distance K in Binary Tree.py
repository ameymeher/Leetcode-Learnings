# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1. Sometimes you gotta add the parent pointer
"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def add_parent(root,parent):
            if root:
                root.parent = parent
                add_parent(root.left,root)
                add_parent(root.right,root)

        add_parent(root,None)

        ans = []

        def dfs():

            visited = set()
            
            def find(root,dist):
                if not root or root.val in visited:
                    return

                visited.add(root.val)

                if dist == 0:
                    ans.append(root.val)
                    return

                find(root.left,dist-1)
                find(root.right,dist-1)
                find(root.parent,dist-1)

            find(target,k)
                
        def bfs():
            queue = [(target,0)]
            visited = set()

            for node,dist in queue:
                if node is None or node.val in visited or dist > k:
                    continue

                visited.add(node.val)

                if dist == k:
                    ans.append(node.val)

                queue.append((node.left,dist+1))
                queue.append((node.right,dist+1))
                queue.append((node.parent,dist+1))

        bfs()
        #dfs()

        return ans
            
