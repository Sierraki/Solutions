class AnimalShelf:

    def __init__(self):
        self.a = [deque(), deque()]

    def enqueue(self, animal: List[int]) -> None:
        self.a[animal[1]].append(animal)

    def dequeueAny(self) -> List[int]:
        if self.a[0] and self.a[1]:
            return (
                self.a[0][0][0] < self.a[1][0][0]
                and self.a[0].popleft()
                or self.a[1].popleft()
            )
        return self.a[0] and self.dequeueCat() or self.dequeueDog()

    def dequeueDog(self) -> List[int]:
        return self.a[1] and self.a[1].popleft() or [-1, -1]

    def dequeueCat(self) -> List[int]:
        return self.a[0] and self.a[0].popleft() or [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
