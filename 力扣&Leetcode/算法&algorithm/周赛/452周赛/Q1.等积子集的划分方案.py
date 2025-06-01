class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def backtrack(start, product, path):
            if product == target and path:
                return path
            for i in range(start, len(nums)):
                num = nums[i]
                if product != 0 and abs(product * num) > abs(target):
                    continue
        
                res = backtrack(i + 1, product * num, path + [num])
                if res is not None:
                    return res
            return None
    
        
        ans = backtrack(0, 1, [])
        if ans==None:
            return False
        a = [x for x in nums if x not in ans]
        cnt1 = 1
        cnt2 = 1
        for i in ans:
            cnt1 *= i
        for i in a:
            cnt2 *= i
        print(cnt1 == cnt2)
        return (cnt1 == cnt2)