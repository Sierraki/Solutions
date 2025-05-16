from collections import Counter, defaultdict


word = "aeiou"
k = 0

cnt = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
fcnt = Counter()
su = 0  # total cnt

for i in word[: (5 + k)]:
    if i in cnt:
        cnt[i] += 1
    else:
        fcnt[i] += 1
if len(cnt) >= 5 and len(fcnt) == k and min(fcnt.values()) == 1 :
    su += 1
wl = k + 5
for i in range(k + 5, len(word)):
    # remove
    if word[i - wl] in cnt:
        cnt[word[i - wl]] -= 1
    else:
        fcnt[word[i - wl]] -= 1
        if fcnt[word[i - wl]] == 0:
            del fcnt[word[i - wl]]

    # add
    if word[i] in cnt:
        cnt[word[i]] += 1
    else:
        fcnt[word[i]] += 1

    if min(cnt.values()) >= 1 and len(fcnt) == k and min(fcnt.values()) == 1:
        su += 1
    print(word[i - wl + 1 : i + 1], su, cnt, fcnt)
print(su)
