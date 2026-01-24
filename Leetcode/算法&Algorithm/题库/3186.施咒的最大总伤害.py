class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        power = sorted(list(set(power)))
        dp = [0] * (len(power))
        dp[0] = cnt[power[0]] * power[0]
        pin = 0
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], cnt[power[i]] * power[i])
            while power[i] - power[pin] >= 3:
                if power[i] - power[pin] <= 2:
                    break
                pin += 1
            while power[i] - power[pin] <= 2 and pin > 0:
                if power[i] - power[pin] >= 3:
                    break
                pin -= 1
            if power[i] - power[pin] >= 3:
                dp[i] = max(dp[i], cnt[power[i]] * power[i] + dp[pin])
        return max(dp)
