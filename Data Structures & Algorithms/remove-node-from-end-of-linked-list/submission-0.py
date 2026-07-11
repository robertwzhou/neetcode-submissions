# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        sz = 0
        while pointer:
            sz += 1
            pointer = pointer.next
        if sz == n:
            return head.next
        pointer = head
        while sz > n + 1:
            pointer = pointer.next
            sz -= 1
        pointer.next = pointer.next.next
        return head