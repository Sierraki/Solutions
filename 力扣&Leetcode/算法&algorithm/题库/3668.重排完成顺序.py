class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        cnt = Counter(friends)
        ans = []
        for i in order:
            if i in cnt:
                ans.append(i)
        return ans
