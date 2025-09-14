class Solution:
    def interpret(self, command: str) -> str:
        a = []
        for idx, i in enumerate(command):
            if i == "G":
                a.append(i)
            elif i == "(":
                if command[idx + 1] == "a":
                    a.append("al")
                else:
                    a.append("o")
        return "".join(a)
