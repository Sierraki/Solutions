class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cnt = Counter(ranks)
        res = [i for i in cnt.values()]
        if len(set(suits)) == 1:
            return "Flush"
        elif 3 in res or 4 in res:
            return "Three of a Kind"
        elif max(res) == 1:
            return "High Card"
        else:
            return "Pair"
