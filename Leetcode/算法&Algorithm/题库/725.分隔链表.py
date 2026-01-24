# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        pin = head
        while pin:
            n += 1
            pin = pin.next
        cnt = n // k
        big = n % k  # n//k+1
        small = k - big  # n//k
        ans = []
        left = head
        right = head
        for i in range(big):
            for j in range(n // k):
                right = right.next
            tmp = right.next
            right.next = None
            ans.append(left)
            left = tmp
            right = tmp
        if n // k == 0:
            for _ in range(small):
                ans.append(None)
        else:
            for i in range(small):
                for j in range(n // k - 1):
                    right = right.next
                tmp = right.next
                right.next = None
                ans.append(left)
                left = tmp
                right = tmp
        return ans
