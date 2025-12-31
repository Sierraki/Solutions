# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            pin = head
            tail = None
            while pin:
                tmp = pin.next
                pin.next = tail
                tail = pin
                pin = tmp
            return tail

        tail = rev(head)
        pin = tail
        while pin:
            pin.val = pin.val * 2
            pin = pin.next
        pin = tail
        while pin:
            if pin.next == None:
                if pin.val >= 10:
                    pin.val = int(pin.val % 10)
                    pin.next = ListNode(1)
                break
            else:
                if pin.val >= 10:
                    pin.val = int(pin.val % 10)
                    pin.next.val += 1
                pin = pin.next
        return rev(tail)
