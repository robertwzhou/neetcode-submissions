# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if curr.next:
                temp = curr.next
                curr.next = prev
                return reverse(curr, temp)
            else:
                curr.next = prev
                return curr
        if head:
            return reverse(None, head)
        return head