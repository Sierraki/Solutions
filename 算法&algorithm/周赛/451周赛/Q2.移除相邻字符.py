class Solution:
    def resultingString(self, s: str) -> str:
        def check(a, b):
            return abs(ord(a) - ord(b)) == 1 or {a, b} == {"a", "z"}

        stack = []
        for c in s:
            if stack and check(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        print("".join(stack))
        return "".join(stack)
