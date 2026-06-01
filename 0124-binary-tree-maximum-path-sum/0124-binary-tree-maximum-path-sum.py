# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # post-order traversal 
        global_max = float('-inf')

        def dfs(node):
            nonlocal global_max
            if not node: return 0

            left_branch = max(0, dfs(node.left))
            right_branch = max(0, dfs(node.right))
            curr_arch = node.val + left_branch + right_branch
            
            global_max = max(global_max, curr_arch)
            return node.val + max(left_branch, right_branch)
        
        dfs(root)
        return global_max

