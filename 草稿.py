from collections import Counter, defaultdict
import bisect

strs = ["flower", "flow", "flight"]

ans = []
strs.sort()
for i in range(len(strs[0])):
    if strs[0][i] == strs[-1][i]:
        ans.append(strs[0][i])
    else:
        break
print(strs)
ans = "".join(ans)

print(ans)
