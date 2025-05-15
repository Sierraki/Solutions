import bisect
from collections import Counter, defaultdict
from itertools import count
from datetime import datetime


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link(value):
    if not value:
        return None
    head = ListNode(value[0])
    pin = head
    for i in value[1:]:
        pin.next = ListNode(i)
        pin = pin.next
    return head


def printf(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        pin = head

        if l1.val <= l2.val:
            pin.next = l1
            l1 = l1.next
        else:
            pin.next = l2
            l2 = l2.next
        pin = pin.next

        return head


eg = Solution()
print(printf(eg.mergeTwoLists(link([1, 2, 4]), link([1, 2, 4]))))
