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
        
        old_to_new = {}
        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            new_copy = Node(curr.val)
            old_to_new[curr] = new_copy

            for neighbor in curr.neighbors:
                new_copy.neighbors.append(dfs(neighbor))
            return new_copy
        
        return dfs(node)