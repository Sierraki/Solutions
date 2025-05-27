class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.len = 0
        # print(self.dummy)

    def get(self, index: int) -> int:
        pin = self.dummy
        if index + 1 > self.len:
            return -1
        else:
            while index >= 0:
                pin = pin.next
                index -= 1
            return pin.val
        # print(pin.val)

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.dummy.next
        self.dummy.next = new
        self.len += 1
        # print(self.dummy)

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        pin = self.dummy
        while pin.next != None:
            pin = pin.next
        pin.next = new
        self.len += 1
        # print(self.dummy)

    def addAtIndex(self, index: int, val: int) -> None:
        pin = self.dummy
        new = ListNode(val)
        index -= 1
        if index + 1 <= self.len:
            while index >= 0:
                print(pin.val)
                pin = pin.next
                index -= 1
            new.next = pin.next
            pin.next = new
            self.len += 1
        # print(self.dummy)

    def deleteAtIndex(self, index: int) -> None:
        pin = self.dummy
        if index + 1 <= self.len:
            while index > 0:
                pin = pin.next
                index -= 1
            pin.next = pin.next.next
            self.len -= 1
        # print(self.dummy)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
