# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node: return True
            valid_left, valid_right = True, True
            
            if not (left < node.val < right):
                return False
            if node.left:
                valid_left = dfs(node.left, left, node.val)
            if node.right:
                valid_right = dfs(node.right, node.val, right)
                
            return valid_left and valid_right
        return dfs(root, float('-inf'), float('inf'))


