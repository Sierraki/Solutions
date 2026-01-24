# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        dummy = ListNode()
        dummy.next = list1
        p1 = dummy
        cnt = 0
        while p1.next:
            if cnt == a:
                break
            cnt += 1
            p1 = p1.next
        tmp = p1.next
        p1.next = list2
        # print(list1)
        while p1.next:
            p1 = p1.next
        # print(p1)# last node
        # print(tmp)
        pin = tmp
        while pin:
            if cnt == b:
                break
            pin = pin.next
            cnt += 1
        pin = pin.next
        p1.next = pin
        return list1
