class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        tar = [idx for idx in range(len(s)) if s[idx] == c]
        nums = list(range(len(s)))
        if len(tar) > 1:
            pin = 0
            for i in range(len(nums)):
                while nums[i] >= tar[pin] and pin < len(tar) - 1:
                    pin += 1

                if pin == len(tar) - 1 or nums[i] < tar[pin] or i == len(nums) - 1:
                    if pin >= 1:
                        nums[i] = min(abs(i - tar[pin]), abs(i - tar[pin - 1]))
                    else:
                        nums[i] = abs(i - tar[pin])
                elif nums[i] == tar[pin]:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = abs(nums[i] - tar[0])
        return nums
