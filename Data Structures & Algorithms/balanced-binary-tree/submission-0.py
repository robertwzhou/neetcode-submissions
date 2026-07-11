# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced_height(root: Optional[TreeNode]):
            if root == None:
                return [True, 0]
            l_b, l_h = balanced_height(root.left)
            r_b, r_h = balanced_height(root.right)
            b = l_h == r_h or l_h + 1 == r_h or r_h + 1 == l_h
            return [b and l_b and r_b, max(l_h, r_h) + 1]
        return balanced_height(root)[0]