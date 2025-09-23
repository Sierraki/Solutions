def slove(nums=str):
    res = ""
    for i in nums:
        if i.lower() not in "yaeiou" and i.isalpha():
            res += "." + i.lower()
    print(res)


slove(input())
