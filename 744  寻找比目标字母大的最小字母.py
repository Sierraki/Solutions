class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nums = letters
        nums.sort()
        for i in nums:
            if i > target:
                return i
                break
        else:
            return letters[0]
