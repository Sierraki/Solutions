class Solution:
    def countOddLetters(self, n: int) -> int:
        cnt1 = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }
        res = ""
        for i in str(n):
            res += cnt1[int(i)]
        cnt = Counter(res)
        return sum([1 for i in cnt.keys() if cnt[i] % 2 == 1])
