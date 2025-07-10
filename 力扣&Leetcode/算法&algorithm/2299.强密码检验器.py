class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        c2 = False
        c3 = False
        c4 = False
        c5 = False
        c6 = True
        for i in password:
            if i.isalpha():
                if i == i.lower():
                    c2 = True
                elif i == i.upper():
                    c3 = True
            elif i.isdigit():
                c4 = True
            elif i in "!@#$%^&*()-+":
                c5 = True
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                c6 = False
        return c2 == c3 == c4 == c5 == c6 == True
