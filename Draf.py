class Solution:
    def dell(self, s: str):
        s = [i for i in s]
        pin = len(s) - 2
        while pin >= 0:
            if (s[pin] == "C" and s[pin + 1] == "D") or (
                s[pin] == "A" and s[pin + 1] == "B"
            ):
                del s[pin]
                del s[pin]
                pin -= 2
            else:
                pin-=1
        return s
    def minLength(self, s: str) -> int:
        last=cur=len(self.s)
        while cur>=last:
            
        


eg = Solution()

eg.minLength("ABFCACDB")
