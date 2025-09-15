class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in words:
            res.extend(i.split(separator))
        res = [i for i in res if i != ""]
        return res
