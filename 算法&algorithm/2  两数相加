# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.insert(0, l1.val)
            l1 = l1.next
        while l2:
            b.insert(0, l2.val)
            l2 = l2.next
        a = "".join(map(str, a))
        b = "".join(map(str, b))
        t = str(int(a) + int(b))
        print(t)
        bb = []
        for i in range(len(t) - 1, -1, -1):
            bb.append(int(t[i]))

        def bulid(listt):
            head = ListNode(listt[0])
            pin = head
            for i in range(1, len(listt)):
                pin.next = ListNode((listt[i]))  # 先赋值
                pin = pin.next  # 再移动
            return head

        return bulid(bb)
