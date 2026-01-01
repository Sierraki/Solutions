# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for i in lists:
            pin = i
            while pin:
                nums.append(pin.val)
                pin = pin.next
        nums.sort()
        dummy = ListNode()
        pin = dummy
        for i in nums:
            pin.next = ListNode(i)
            pin = pin.next
        return dummy.next
