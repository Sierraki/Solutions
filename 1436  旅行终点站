class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = [i[0] for i in paths]
        end = [i[-1] for i in paths]
        for i in end:
            if i not in start:
                return i
