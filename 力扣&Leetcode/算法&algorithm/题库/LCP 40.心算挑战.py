class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        mx = sum(cards[:cnt])
        ans1 = ans2 = 0
        list1 = [i for i in cards[:cnt] if i % 2 == 1]
        list2 = [i for i in cards[cnt:] if i % 2 == 0]
        list3 = [i for i in cards[:cnt] if i % 2 == 0]
        list4 = [i for i in cards[cnt:] if i % 2 == 1]
        if mx % 2 == 1:
            # 选出最小的奇数，换上其他的最大偶数
            tar = min(list1)
            if not list2:
                ans1 = 0
            else:
                alt = max(list2)
                ans1 = mx - tar + alt
            # 选出最小的偶数，换上其他最大的奇数
            if not list3:
                ans2 = 0
            else:
                tar = min(list3)
                if not list4:
                    ans2 = 0
                else:
                    alt = max(list4)
                    ans2 = mx - tar + alt
        ans = 0
        for i in [mx, ans1, ans2]:
            if i % 2 == 0:
                ans = max(i, ans)
        return ans
