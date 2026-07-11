# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        dummy = ListNode(next=l1)
        l = dummy
        carry = 0
        while l.next and l2:
            s = l.next.val + l2.val + carry
            carry = s // 10
            l.next.val = s % 10
            l = l.next
            l2 = l2.next
        if l2:
            l.next = l2
        while l.next and carry:
            s = l.next.val + carry
            carry = s // 10
            l.next.val = s % 10
            l = l.next
        if carry:
            l.next = ListNode(carry)
        return dummy.next