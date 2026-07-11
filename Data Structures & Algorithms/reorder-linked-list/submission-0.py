# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        prev = slow.next = None
        # reverse
        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp
        # merge
        h2 = prev
        while h2:
            t1, t2 = head.next, h2.next
            head.next = h2
            h2.next = t1
            head, h2 = t1, t2