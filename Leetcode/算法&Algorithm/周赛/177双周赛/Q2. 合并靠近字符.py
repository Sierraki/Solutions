class Solution:
    def mergeCharacters(self, s: str, k: int) -> str: 
        seen = Counter()
        ans = []
        for i  in s:
            cur_idx = len(ans) + 1
            if i in seen:
                if cur_idx - seen[i]>k:
                    seen[i] = cur_idx
                    ans.append(i)
            else:
                seen[i] = cur_idx
                ans.append(i)
        return ''.join(ans) 