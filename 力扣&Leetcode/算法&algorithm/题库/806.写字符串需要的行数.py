class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cnt = dict(zip([chr(i) for i in range(ord("a"), ord("z") + 1)], widths))
        layer_cnt = 1
        cur = 0
        for i in s:
            if cur + cnt[i] > 100:
                layer_cnt += 1
                cur = cnt[i]
            else:
                cur += cnt[i]
        return [layer_cnt, cur]
