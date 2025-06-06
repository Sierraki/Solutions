# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        if not l1 or not l2:
            return l1 or l2
        else:
            p1, p2 = l1, l2
            while p1:
                a.append(str(p1.val))
                p1 = p1.next
            while p2:
                b.append(str(p2.val))
                p2 = p2.next
            res1 = "".join(a)
            res2 = "".join(b)
            res = str(int(res1) + int(res2))
            dummy = ListNode()
            pin = dummy
            for i in res:
                pin.next = ListNode(int(i))
                pin = pin.next
            return dummy.next
