class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.next.val

    def insertHead(self, val: int) -> None:
        head = ListNode(val, self.dummy.next)
        self.dummy.next = head
        if self.size == 0:
            self.tail = head
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        curr = self.dummy
        while index > 0:
            curr = curr.next
            index -= 1
        # what if tail must be removed?
        if self.tail == curr.next:
            self.tail = curr
        curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.dummy.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values