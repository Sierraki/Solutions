class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        pin = head
        while l1 and l2:
            if l1.val <= l2.val:
                pin.next = l1
                l1 = l1.next
            else:
                pin.next = l2
                l2 = l2.next
            pin = pin.next
        pin.next = l1 or l2
        return head.next
