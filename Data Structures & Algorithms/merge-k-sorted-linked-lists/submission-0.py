# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [[first_node.val, i, first_node] for i, first_node in enumerate(lists) if first_node]
        heapq.heapify(heap)
        dummy = ListNode()
        curr = dummy
        while heap:
            v, i, curr.next = heapq.heappop(heap)
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, [curr.next.val, i, curr.next])
        return dummy.next