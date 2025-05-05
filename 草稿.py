from collections import defaultdict

s = "1010101"
k = 2
cur = 0
left = right = 0
cnt = defaultdict(int)
n = len(s)

while right < n:
    cnt[s[right]] += 1
    if cnt["0"] <= k or cnt["1"] <= k:
        cur += 1
        right += 1
    else:
        cnt.clear()
        left += 1
        right = left

    if right >= n:
        cnt.clear()
        left += 1
        right = left

    # print(s[left : right + 1], cur)
print(cur)
