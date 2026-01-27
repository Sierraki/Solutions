class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        n = len(ranks)
        cnt1 = Counter(ranks)
        tri = False
        dou = False
        for i in cnt1.values():
            if 3 <= i < 5:
                tri = True
            elif 2 <= i < 3:
                dou = True
        if tri:
            return "Three of a Kind"
        if dou:
            return "Pair"
        cnt2 = set(suits)
        if len(cnt2) == 1:
            return "Flush"
        return "High Card"
