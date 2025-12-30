class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        res_count = 0
        for num in range(100, 1000, 2):
            s = str(num)
            d1, d2, d3 = int(s[0]), int(s[1]), int(s[2])
            cur_need = Counter([d1, d2, d3])
            possible = True
            for d, needed_amount in cur_need.items():
                if count[d] < needed_amount:
                    possible = False
                    break
            if possible:
                res_count += 1
        return res_count
