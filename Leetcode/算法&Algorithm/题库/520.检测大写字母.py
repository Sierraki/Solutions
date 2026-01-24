class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        u = 0
        l = 0
        for i in word:
            if i.upper() == i:
                u += 1
            else:
                l += 1
        if l == len(word):
            return True
        elif word[0].upper() == word[0] and u == 1:
            return True
        elif l == 0:
            return True
        else:
            return False


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()
