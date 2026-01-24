class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            longer = str1
            shorter = str2
        else:
            longer = str2
            shorter = str1
        ans = ""
        for i in range(len(shorter)):
            size = i + 1
            tar = shorter[: i + 1]
            if len(longer) % size == 0 and len(shorter) % size == 0:
                if longer == tar * (len(longer) // size) and shorter == tar * (
                    len(shorter) // size
                ):
                    ans = tar
        return ans
