class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        st = True
        for i in range(1, len(words)):
            if words[i][0] != words[i - 1][-1]:
                st = False
        if words[-1][-1] != words[0][0]:
            st = False
        return st
