class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        nums = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        cur = wl = big = left = 0

        for i in range(n):
            cur += nums[i]
            wl += 1
            if cur > maxCost:
                while cur > maxCost:
                    cur -= nums[left]
                    left += 1
                    wl -= 1

            big = max(wl, big)
            # print(nums[left : i + 1], cur, big)

        return big
