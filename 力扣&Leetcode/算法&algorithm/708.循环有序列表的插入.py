"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        new = ListNode(insertVal)
        pin = head
        if not head:
            new.next = new
            return new
        while pin:
            if pin.val <= new.val <= pin.next.val:
                break
            elif pin.val > pin.next.val and (
                new.val > pin.val or new.val < pin.next.val
            ):
                break
            elif pin.next == head:
                break
            pin = pin.next
        new.next = pin.next
        pin.next = new
        return head
