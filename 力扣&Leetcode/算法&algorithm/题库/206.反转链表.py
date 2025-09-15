# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nums = []
        pin = head
        while pin:
            nums.insert(0, pin.val)
            pin = pin.next
        h1 = ListNode()
        pin1 = h1
        for i in nums:
            pin1.next = ListNode(i)
            pin1 = pin1.next
        return h1.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pin = head
        tail = None
        while pin:
            tmp = pin.next
            pin.next = tail
            tail = pin
            pin = tmp
            # print(tail)
        return tail
