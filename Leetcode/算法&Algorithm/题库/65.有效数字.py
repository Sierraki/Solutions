class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {"dig": 2, "sign": 1, "dot": 3},
            {"dig": 2, "dot": 3},
            {"dig": 2, "dot": 4, "exp": 5},
            {"dig": 4},
            {"dig": 4, "exp": 5},
            {"dig": 7, "sign": 6},
            {"dig": 7},
            {"dig": 7},
        ]
        cur = 0
        for i in s:
            if i.isdigit():
                typ = "dig"
            elif i in "+-":
                typ = "sign"
            elif i == ".":
                typ = "dot"
            elif i in "eE":
                typ = "exp"
            else:
                return False
            cur = states[cur].get(typ, "end")
            if cur == "end":
                return False
        return cur in [2, 4, 7]
