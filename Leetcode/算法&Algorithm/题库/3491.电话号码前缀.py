class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers.sort()
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[j].startswith(numbers[i]):
                    return False
                else:
                    pass
        return True
