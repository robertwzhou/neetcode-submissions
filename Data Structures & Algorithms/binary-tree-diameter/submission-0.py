# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_height(root: Optional[TreeNode]) -> List[int]:
            if root == None:
                return [0, 0]
            l_d, l_h = diameter_height(root.left)
            r_d, r_h = diameter_height(root.right)
            d = 0
            if root.left:
                d += l_h
            if root.right:
                d += r_h
            return [max(d, l_d, r_d), max(l_h, r_h) + 1]
        return diameter_height(root)[0]