# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(node: TreeNode):
            # lca, left contains p, right contains q
            if node == None:
                return [None, False, False]
            contains_p = node.val == p.val
            contains_q = node.val == q.val
            l_lca, l_p, l_q = lca(node.left)
            if l_lca:
                return [l_lca, True, True]
            if (contains_p and l_q) or (contains_q and l_p):
                return [node, True, True]
            r_lca, r_p, r_q = lca(node.right)
            if r_lca:
                return [r_lca, True, True]
            if (contains_p and r_q) or (contains_q and r_p):
                return [node, True, True]
            if (l_p and r_q) or (l_q and r_p):
                return [node, True, True]
            return [None, contains_p or l_p or r_p, contains_q or l_q or r_q]
        return lca(root)[0]