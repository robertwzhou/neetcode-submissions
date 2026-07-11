# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        head = list1
        if list1.val < list2.val:
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 == None:
            curr.next = list2
        else:
            curr.next = list1
        return head
        """
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val < list2.val:
            p = list1
            list1 = list1.next
        else:
            p = list2
            list2 = list2.next
        p.next = self.mergeTwoLists(list1, list2)
        return p
        """