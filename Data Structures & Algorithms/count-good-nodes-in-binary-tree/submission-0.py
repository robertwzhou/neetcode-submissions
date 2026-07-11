# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(x: TreeNode, greatest: int) -> int:
            if x == None:
                return 0
            g = 0
            if x.val >= greatest:
                g = 1
            return g + good(x.left, max(x.val, greatest)) + good(x.right, max(x.val, greatest))
        return good(root, root.val)