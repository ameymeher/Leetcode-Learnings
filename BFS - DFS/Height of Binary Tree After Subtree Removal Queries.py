# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        from collections import defaultdict
        from heapq import heappush, heappop

        level_map = defaultdict(list) #{0:[1],1:[3,4],2:[2,6,5],3:[7]}
        node_map = {} #{1:0,3:1,2:2,4:1,6:2,5:2,7:3}

        def postorder(root,h):
            if not root:
                return 0

            left_height = postorder(root.left,h+1)
            right_height = postorder(root.right,h+1)

            node_map[root.val] = h
            max_height = max(left_height,right_height)
            total_height = max_height + h

            heappush(level_map[h],(total_height,root.val))
            if level_map[h] and len(level_map[h]) > 2:
                heappop(level_map[h])
            
            return 1 + max(left_height,right_height)

        postorder(root,0)

        ans_arr = []

        for to_delete in queries:
            level = node_map[to_delete]
            ans = 0
            if len(level_map[level]) == 1:
                ans = level-1
            else:
                for total_height,adjacent_node in level_map[level]:
                    if adjacent_node != to_delete:
                        ans = max(ans,total_height)

            ans_arr.append(ans)

        return ans_arr