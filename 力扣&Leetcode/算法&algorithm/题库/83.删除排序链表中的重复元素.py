# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        current = head
        while current:
            if current.val not in cnt:
                cnt[current.val] += 1
                prev = current  # 保留前驱节点
            else:
                prev.next = current.next  # 跳过当前节点
            current = current.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        while head.next and head.val == head.next.val:
            head = head.next
        cnt = Counter()
        pin = head
        while pin.next:
            if pin.next.val not in cnt:
                cnt[pin.next.val] = 1
                pin = pin.next
            else:
                pin.next = pin.next.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cnt = Counter()
        pin = head
        dummy = ListNode()
        p1 = dummy
        while pin:
            if pin.val not in cnt:
                cnt[pin.val] += 1
                p1.next = ListNode(pin.val)
                p1 = p1.next
            pin = pin.next
        return dummy.next
