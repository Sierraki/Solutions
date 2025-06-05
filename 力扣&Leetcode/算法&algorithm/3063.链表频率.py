# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        pin=head
        while pin:
            nums.append(pin.val)
            pin=pin.next
        cnt=Counter(nums)
        res=[cnt[i] for i in cnt]
        dummy=ListNode()
        pin=dummy
        for i in res:
            pin.next=ListNode(i)
            pin=pin.next
        return dummy.next