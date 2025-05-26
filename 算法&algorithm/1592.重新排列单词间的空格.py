class Solution:
    def reorderSpaces(self, text: str) -> str:
        blank_cnt = text.count(" ")
        words = text.split()
        word_cnt = len(words)
        if word_cnt == 1:
            return words[0] + " " * blank_cnt
        space_between = blank_cnt // (word_cnt - 1)
        extra_space = blank_cnt % (word_cnt - 1)
        result = (" " * space_between).join(words)
        result += " " * extra_space
        return result
