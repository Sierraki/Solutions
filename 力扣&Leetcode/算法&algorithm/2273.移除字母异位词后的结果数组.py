class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        pin = 0
        while pin < len(words) - 1:
            if Counter(words[pin]) == Counter(words[pin + 1]):
                del words[pin + 1]
            else:
                pin += 1
        return words
