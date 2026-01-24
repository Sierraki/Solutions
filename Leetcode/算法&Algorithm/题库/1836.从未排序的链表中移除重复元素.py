# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        pin = head
        while pin:
            cnt[pin.val] += 1
            pin = pin.next
        res = [i for i in cnt if cnt[i] <= 1]
        dummy = ListNode()
        pin = dummy
        for i in res:
            pin.next = ListNode(i)
            pin = pin.next
        return dummy.next
