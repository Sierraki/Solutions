class Solution:
    def makeGood(self, s: str) -> str:
        def fun(a=str, b=str) -> bool:
            if a.lower() == b.lower():
                if a.isupper() and b.islower() or (a.islower() and b.isupper()):
                    return True
            return False

        a = deque([i for i in s])
        b = deque([])

        while a:
            cur = a.popleft()
            if not b:
                b.append(cur)
            else:
                if fun(b[-1], cur):
                    b.pop()
                else:
                    b.append(cur)
        return "".join(b)
