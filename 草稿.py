s = "aabccabba"

n = len(s)
left, right = 0, n - 1
while left <= right:
    while s[left] == s[right]:
        if s[left] == s[left + 1]:
            left += 1
        if s[right] == s[right - 1]:
            right -= 1
    while s[left+1] == s[right-1]:
        left+=1
        right-=1
    print(left, right)
