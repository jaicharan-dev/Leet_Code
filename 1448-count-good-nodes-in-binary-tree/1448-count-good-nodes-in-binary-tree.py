# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node, limit):
            nonlocal good_nodes
            if not node: return
            if node.val >= limit:
                good_nodes += 1
                limit = node.val
            
            dfs(node.left, limit)
            dfs(node.right, limit)
            return
        dfs(root, float("-inf"))
        return good_nodes
          
