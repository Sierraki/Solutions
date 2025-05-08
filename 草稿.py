s = "cabaabac"

s = [i for i in s]
n = len(s)
left, right = 0, n - 1

while left < right:
    while s[left] == s[right]:
        right -= 1
    while s[left] == s[left + 1]:
        left += 1
    if s[left] != s[left + 1]:
        left += 1

    if s[left] != s[right]:
        break
print(right - left + 1)
