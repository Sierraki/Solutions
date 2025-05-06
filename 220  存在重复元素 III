class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        k = indexDiff + 1
        st = False
        n = len(nums)
        if k > n:
            nums.sort()
            for i in range(1, n):
                if abs(nums[i] - nums[i - 1]) <= valueDiff:
                    st = True
                    break
        else:
            a = SortedList(nums[:k])
            if k <= n:
                for i in range(1, k):
                    if abs(a[i] - a[i - 1]) <= valueDiff:
                        st = True
                        break

            if k < n:
                for i in range(k, n):
                    # add
                    a.add(nums[i])
                    # remove
                    a.remove(nums[i - k])
                    lc = bisect.bisect_right(a, nums[i]) - 1
                    if lc == k - 1:
                        if abs(a[lc] - a[lc - 1]) <= valueDiff:
                            st = True
                            break
                    elif lc == 0:
                        if abs(a[lc] - a[lc - 1]) <= valueDiff:
                            st = True
                            break
                    else:
                        if (
                            abs(a[lc] - a[lc - 1]) <= valueDiff
                            or abs(a[lc] - a[lc + 1]) <= valueDiff
                        ):
                            st = True
                            break

        return st
