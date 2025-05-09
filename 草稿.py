from collections import Counter, defaultdict
import bisect

<<<<<<< HEAD
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

=======
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]

n = len(words[0])  # 单个单词长度
k = len(words) * n  # 窗口长度
target = Counter(words)  # 对照目标
left, right = 0, k - 1
ans = []  # 答案列表


while right < len(s):
    tmp = defaultdict(int)  # 临时表
    for i in range(left, right + 1, n):
        if s[i : i + n] not in target:
            break
        tmp[s[i : i + n]] += 1
    if tmp == target:
        ans.append(left)
    left += 1
    right += 1
>>>>>>> c06d07604492383854bf04633e5541ca710f4ed8
print(ans)
