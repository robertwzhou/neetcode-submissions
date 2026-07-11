# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
            # curr exists
            h = curr
            if curr.next:
                h = reverse(curr, curr.next)
            curr.next = prev
            return h
        if head:
            return reverse(None, head)
        return head