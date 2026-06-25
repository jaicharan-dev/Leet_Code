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
        old_to_new = {None:None}
        def dfs(node):
            if not node in old_to_new:
                copy = Node(node.val)
                old_to_new[node] = copy

                for neighbor in node.neighbors:
                    copy.neighbors.append(dfs(neighbor))
            
            return old_to_new[node]
        return dfs(node)

