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
        
        if not node : return None
        old_to_new = {}
        # node maker - make our graph here
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor)) 
            return new_node
            
        return dfs(node)
        
        # the idea is to keep an adjacency dict to map the lod node to the new nodes
        # why to map the old nodes to the new ones, 
        # because its it not only about creation if nonexistant ones
        # they also have to connect later ( neighbors ) when creating other nodes
        # here is our adj_list ( i dont knw if you call this an adjacency dict or something else)
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