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
        """
        Creates a deep copy (clone) of a connected, undirected graph.

        --- ALGORITHM STRATEGY: GRAPH CLONING VIA DFS & CLONE MAPPING ---
        Cloning a graph requires a careful two-step balance for every node:
        1. Copying the node's individual identity (its integer value).
        2. Copying the node's structural relationships (its pointers to neighbors).

        We track this using a Morphism Map (`old_to_new`) which maps:
        Old Node Reference -> New Node Reference

        When `dfs(curr)` runs:
        - BASE CASE: If `curr` is already in our map, it means this node was cloned 
          on a previous path. We return its clone immediately to avoid duplicates 
          and break infinite cyclical loops.
        - EXPLORATION: If it's a fresh node, we instantiate its clone and immediately 
          cache it in our map. Then, we look at the old node's neighbors. If a neighbor 
          cloned instance doesn't exist yet, we invoke the `dfs` machine to dynamically 
          build it out, appending the resulting cloned references to our new node's list.

        --- TIME & SPACE COMPLEXITY ---
        - Time Complexity: O(V + E), where V is the number of vertices (nodes) and E 
          is the number of edges. We visit every single node and traverse every single 
          edge connection exactly once.
        - Space Complexity: O(V) auxiliary space. The `old_to_new` map stores exactly 
          V key-value mappings. Additionally, the implicit recursion stack can grow 
          up to size O(V) in a deeply linked linear graph layout.
        """        

        if not node : return None
        old_to_new = {}
        # node maker - make our graph here
        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
            
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            for neighbor in curr.neighbors:
                new_node.neighbors.append(dfs(neighbor)) 
            return new_node

        return dfs(node)
        
        # the idea is to keep an clone map to map the lod node to the new nodes
        # why to map the old nodes to the new ones, 
        # because its it not only about creation if nonexistant ones
        # they also have to connect later ( neighbors ) when creating other nodes
        # here is our clone map
        # the dfs is basically the copy maker
        # if youo give it a node of the graph (usually its root)
        # it will give you the deep copy of the graph
        # in other words construct the whole structure again 
            # first before making a new copy
            # we need to check if the node already exists
            # if yes then use that only
            # if it does not exist then we make a copy
            # create a new node with the same value ( deep copy )
            # and add it to the map
            # we also need to link neigbors to the new node we just created
            # but what if the new neighbor is not made yet
            # then run the node maker (dfs) on the old neighbor
            # this is the recursion step 
            # once the neighbors are connected return the new_node
        # run the node maker on the root and return the new graph