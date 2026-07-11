"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        head_c = Node(head.val)
        curr = head
        curr_c = head_c
        original_to_copy = {head : head_c}
        while curr.next:
            curr = curr.next
            curr_c.next = Node(curr.val)
            curr_c = curr_c.next
            original_to_copy[curr] = curr_c
        # deal with random
        curr = head
        curr_c = head_c
        while curr:
            if curr.random:
                curr_c.random = original_to_copy[curr.random]
            curr = curr.next
            curr_c = curr_c.next
        return head_c
        