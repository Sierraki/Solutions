class Foo:
    def __init__(self):
        self.fi = False
        self.se = False
        self.th = False

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.fi = True

    def second(self, printSecond: "Callable[[], None]") -> None:
        while not self.fi:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.se = True

    def third(self, printThird: "Callable[[], None]") -> None:
        while not self.se or not self.fi:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.th = True
