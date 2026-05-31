"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, length):
            first_val = grid[r][c]
            is_uniform = True
            for i in range(length):
                for j in range(length):
                    if grid[r+i][c+j] != first_val:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
            
            if is_uniform:
                return Node(val=(first_val==1), isLeaf=True,
                            topLeft=None, topRight=None, 
                            bottomLeft=None, bottomRight=None)
            
            half = length // 2
            topLeft = build(r, c, half)
            topRight = build(r, c+half, half)
            bottomLeft = build(r+half, c, half) 
            bottomRight = build(r+half, c+half, half)

            return Node(val=True, isLeaf=False,
                        topLeft=topLeft, topRight=topRight, 
                        bottomLeft=bottomLeft, bottomRight=bottomRight)
        return build(0, 0, len(grid))