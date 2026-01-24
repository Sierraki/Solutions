# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # 导入函数
        def rel(head: Optional[ListNode]) -> Optional[ListNode]:
            pin = head
            tail = None
            while pin:
                tmp = pin.next
                pin.next = tail
                tail = pin
                pin = tmp
            return tail

        # 头尾加0
        new = ListNode(0)
        tail = ListNode(0)
        new.next = head
        head = new
        pin = head
        while pin.next:
            pin = pin.next
        pin.next = tail
        # 切割最后部分 tmp1
        pin = head
        while right > 0:
            right -= 1
            pin = pin.next
        tmp1 = pin.next
        pin.next = None
        # 切割中间 tmp2
        pin = head
        while left > 1:
            left -= 1
            pin = pin.next
        tmp2 = pin.next
        pin.next = None
        tmp2 = rel(tmp2)
        # 处理head和tmp1的0部分
        pin = head
        while pin.next:
            pin = pin.next
        pin.next = tmp2
        while pin.next:
            pin = pin.next
        pin.next = tmp1
        while pin.next.next:
            pin = pin.next
        pin.next = None
        return head.next
