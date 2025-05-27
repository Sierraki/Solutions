# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pin = dummy
        while pin.next:
            if pin.next.val == val:
                pin.next = pin.next.next
            else:
                pin = pin.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head.val == val:
            head = head.next
        pin = head
        while pin.next:
            if pin.next.val == val:
                pin.next = pin.next.next
            else:
                pin = pin.next
        return head
