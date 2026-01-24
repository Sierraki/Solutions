class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cnt = {"+", "-", "*", "/"}
        res = deque([])
        tokens = deque(tokens)
        while tokens:
            cur = tokens.popleft()
            if cur not in cnt:
                res.append(cur)
            else:
                a1 = int(res.pop())
                a2 = int(res.pop())
                if cur == "+":
                    ans = a1 + a2
                elif cur == "-":
                    ans = a2 - a1
                elif cur == "*":
                    ans = a2 * a1
                elif cur == "/":
                    if a2 / a1 > 0:
                        ans = floor(a2 / a1)
                    else:
                        ans = ceil(a2 / a1)
                res.append(ans)
        return int(res[-1])
