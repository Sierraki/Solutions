# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        p1 = dummy.next
        p2 = dummy.next.next
        while p2:
            tmp = p2.next
            prev.next = p2
            p2.next = p1
            p1.next = tmp
            if not tmp:
                break
            p1 = tmp
            p2 = tmp.next
            if not p2:
                break
            prev = prev.next.next
        return dummy.next
