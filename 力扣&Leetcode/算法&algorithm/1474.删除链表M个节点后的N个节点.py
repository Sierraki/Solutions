# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        cnt1 = 0  # save
        cnt2 = 0  # del
        dummy = ListNode()
        dummy.next = head
        pin = dummy
        while pin:
            # check
            if cnt1 < m:
                cnt1 += 1
                pin = pin.next
            else:
                # del
                if pin.next:
                    pin.next = pin.next.next
                    cnt2 += 1
                    if cnt2 == n:
                        cnt1 = 0
                        cnt2 = 0
                else:
                    return dummy.next
        return dummy.next
