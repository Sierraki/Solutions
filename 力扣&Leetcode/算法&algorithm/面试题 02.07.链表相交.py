# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        na, nb = 0, 0
        pina, pinb = headA, headB
        while pina:
            na, pina = na + 1, pina.next
        while pinb:
            nb, pinb = nb + 1, pinb.next
        dif = abs(na - nb)

        if nb >= na:
            while dif > 0:
                dif, headB = dif - 1, headB.next
        else:
            while dif > 0:
                dif, headA = dif - 1, headA.next
        p1, p2 = headA, headB
        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1, p2 = p1.next, p2.next
