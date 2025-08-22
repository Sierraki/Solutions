class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        times = int((-1 + (1 + 8 * candies) ** 0.5) // 2)
        res = [0] * (num_people)
        if times <= num_people:
            for i in range(len(res)):
                if candies >= i + 1:
                    res[i] = i + 1
                    candies -= i + 1
                else:
                    res[i] = candies
                    return res
        else:
            # fib阶数
            tim = int((-1 + (1 + 8 * candies) ** 0.5) // 2)
            # 循环次数
            c = tim // num_people
            res = [i for i in range(1, num_people + 1)]
            if c > 1:
                for i in range(len(res)):
                    res[i] += (c - 1) * num_people
            cnt = [0] * len(res)
            for idx, i in enumerate(res, start=1):
                cnt[idx - 1] = (i + idx) * c // 2
            res = cnt
            # 循环后剩下的糖果
            left = candies - sum(res)
            print(left)
            # 开始计数的数量
            start = c * num_people + 1
            for idx, i in enumerate(res):
                if left >= start:
                    res[idx] += start
                    left -= start
                    start += 1
                else:
                    res[idx] += left
                    return res
