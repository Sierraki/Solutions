# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        n1, n2 = 0, 0
        while p1:
            n1 += 1
            p1 = p1.next
        while p2:
            n2 += 1
            p2 = p2.next
        if n1 > n2:
            while n1 > n2:
                headA = headA.next
                n1 -= 1
        else:
            while n1 < n2:
                headB = headB.next
                n2 -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        else:
            return None
