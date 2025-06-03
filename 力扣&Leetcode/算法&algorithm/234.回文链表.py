# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        pin = head
        n = 0
        while pin:
            a.append(pin.val)
            pin = pin.next
            n += 1
        left, right = 0, n - 1
        st = True
        while left != right and left < n // 2:
            if a[left] == a[right]:
                left += 1
                right -= 1
            else:
                st = False
                break
        print(st)
        return st
