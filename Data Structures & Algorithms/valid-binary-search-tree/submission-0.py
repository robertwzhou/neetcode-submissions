# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # smallest val, node, largest val
        def valid(smallest, node, largest):
            if node == None:
                return True
            if node.val <= smallest or node.val >= largest:
                return False
            return valid(smallest, node.left, node.val) and valid(node.val, node.right, largest)
        return valid(float("-inf"), root, float("inf"))