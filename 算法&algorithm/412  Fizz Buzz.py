class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                i = "FizzBuzz"
            elif i % 3 == 0 and i % 5 != 0:
                i = "Fizz"
            elif i % 3 != 0 and i % 5 == 0:
                i = "Buzz"
                a.append(str(i))
            else:
                i = i
                a.append(str(i))
        return a
