# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def dfs(left, right):
            if left > right:
                return None
            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder)-1)