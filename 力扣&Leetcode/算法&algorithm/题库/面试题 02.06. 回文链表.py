# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        n = 0
        pin = head
        while pin:
            a.append(pin.val)
            pin = pin.next
            n += 1
        left, right = 0, n - 1
        while left < right:
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        return True
