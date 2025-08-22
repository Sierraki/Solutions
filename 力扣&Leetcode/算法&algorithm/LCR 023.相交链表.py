# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        na = nb = 0
        pa, pb = headA, headB
        while pa or pb:
            if pa:
                pa = pa.next
                na += 1
            if pb:
                pb = pb.next
                nb += 1
        pa, pb = headA, headB
        dif = abs(na - nb)
        if na > nb:
            for _ in range(dif):
                pa = pa.next
        else:
            for _ in range(dif):
                pb = pb.next

        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa
