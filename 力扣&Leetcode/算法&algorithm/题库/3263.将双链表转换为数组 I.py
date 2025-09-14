"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
    def toArray(self, root: "Optional[Node]") -> List[int]:
        nums = []
        pin = root
        while pin:
            nums.append(pin.val)
            pin = pin.next
        return nums
