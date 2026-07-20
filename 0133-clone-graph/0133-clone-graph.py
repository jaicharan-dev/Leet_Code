"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        old_to_new = {None : None}
        def dfs(root):
            if root in old_to_new:
                return old_to_new[root]

            copy = Node(root.val)
            old_to_new[root] = copy
            for neighbor in root.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)