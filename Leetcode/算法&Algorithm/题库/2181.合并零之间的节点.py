# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pin = head
        res = []
        s = 0
        while pin:
            if pin.val == 0:
                if s != 0:
                    res.append(s)
                s = 0
            s += pin.val
            pin = pin.next
        print(res)
        dummy = ListNode()
        pin = dummy
        for i in res:
            pin.next = ListNode(i)
            pin = pin.next
        return dummy.next
