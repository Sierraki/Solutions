# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pin = dummy
        nums = set()
        while pin.next:
            if pin.next.val not in nums:
                nums.add(pin.next.val)
                pin = pin.next
            else:
                pin.next = pin.next.next
        return dummy.next
