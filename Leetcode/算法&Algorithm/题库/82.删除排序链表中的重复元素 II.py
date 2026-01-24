# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        pin = head
        while pin:
            cnt[pin.val] += 1
            pin = pin.next
        tar = []
        for i in cnt:
            if cnt[i] == 1:
                tar.append(i)
        dummy = ListNode()
        p1 = dummy
        pin = head
        while pin:
            if pin.val in tar:
                p1.next = ListNode(pin.val)
                p1 = p1.next
            pin = pin.next
        return dummy.next
