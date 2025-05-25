class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        print(cnt)
        cur = 0
        for i in words:
            cnt = Counter(chars)
            for j in i:
                if j in cnt:
                    cnt[j] -= 1
                    if cnt[j] < 0:
                        break
                else:
                    break
            else:
                cur += len(i)
        return cur
