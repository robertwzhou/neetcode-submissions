# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
            while q:
                new_q = deque()
                sublist = []
                while q:
                    node = q.popleft()
                    sublist.append(node.val)
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                res.append(sublist)
                q = new_q
        return res