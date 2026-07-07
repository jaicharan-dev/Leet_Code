# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(node):
            nonlocal max_sum
            if not node: return 0

            left_branch = dfs(node.left) 
            if left_branch < 0:
                left_branch = 0
            right_branch = dfs(node.right) 
            if right_branch < 0:
                right_branch = 0
            
            arc = node.val + left_branch + right_branch
            max_sum = max(max_sum, arc)
            return node.val + max(left_branch, right_branch)

        dfs(root)
        return max_sum