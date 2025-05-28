class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        pin = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                pin.next = ListNode(l2.val)
                l2 = l2.next
            else:
                pin.next = ListNode(l1.val)
                l1 = l1.next
            pin = pin.next
        pin.next = l1 or l2
        return dummy.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val >= p2.val:
                p.next = ListNode(p2.val)
                p2 = p2.next
            else:
                p.next = ListNode(p1.val)
                p1 = p1.next
            p = p.next
            # print(dummy)
        if not p1:
            p.next = p2
        if not p2:
            p.next = p1
        return dummy.next
