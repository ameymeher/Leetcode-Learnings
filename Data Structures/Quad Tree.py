# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        import numpy as np
        grid = np.array(grid)

        m = len(grid)
        n = len(grid[0])

        if m == n == 1:
            return Node(True if grid[0,0] == 1 else False,
                        True,
                        None,None,None,None)

        top_left_node = self.construct(grid[:m//2,:n//2])
        top_right_node = self.construct(grid[:m//2,n//2:])
        bottom_left_node = self.construct(grid[m//2:,:n//2])
        bottom_right_node = self.construct(grid[m//2:,n//2:])

        if (top_left_node.isLeaf and top_right_node.isLeaf and
            bottom_left_node.isLeaf and bottom_right_node.isLeaf) and \
            (top_left_node.val == top_right_node.val ==
            bottom_left_node.val == bottom_right_node.val):

            return Node(top_left_node.val,
                        True,
                        None,None,None,None)
        else:
            return Node(None,False,
                        top_left_node,top_right_node,
                        bottom_left_node,bottom_right_node)