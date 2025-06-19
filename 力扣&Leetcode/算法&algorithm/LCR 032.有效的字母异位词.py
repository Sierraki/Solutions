class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t) and s != t
