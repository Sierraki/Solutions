import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

input = sys.stdin.readline

# num
def ii(): return int(input())
def mii(): return map(int, input().split())
def lmii(): return list(map(int, input().split()))
# string
def lmsi(): return list(map(str, si()))
def si(): return input().strip()
def ms(numss): return "".join(map(str, numss))
# else
def lacc(nums): return list(acc(nums))
def matt(row, col): return [[0] * col for _ in range(row)]
def p(numss):
    for i in numss:
        print(i)
def read_mat(n): return [lmii() for _ in range(n)]



def solve():
    n, h = mii()
    nums = lmii()
    height_limit = [min(x, h) for x in nums]

    def pf(arr):
        sz = len(arr)
        if sz == 0:
            return [] 
        left_mud = [0] * sz
        st = []
        cur_total = 0
        for i in range(sz):
            while st and arr[st[-1]] <= arr[i]:
                rm = st.pop()
                prev = st[-1] if st else -1
                cur_total -= arr[rm] * (rm - prev)
            prev = st[-1] if st else -1
            cur_total += arr[i] * (i - prev)
            st.append(i)
            left_mud[i] = cur_total 
        left_mx = [sz] * sz
        st = []
        for i in range(sz):
            while st and arr[st[-1]] < arr[i]:
                left_mx[st.pop()] = i
            st.append(i)
        up = [[sz] * 19 for _ in range(sz + 1)]
        right_total = [[0] * 19 for _ in range(sz + 1)]

        for i in range(sz):
            up[i][0] = left_mx[i]
            right_total[i][0] = arr[i] * (left_mx[i] - i)

        for i in range(1, 19):
            for j in range(sz):
                nxt = up[j][i - 1]
                up[j][i] = up[nxt][i - 1] if nxt < sz else sz
                right_total[j][i] = right_total[j][i - 1] + \
                    (right_total[nxt][i - 1] if nxt < sz else 0)

        def fun(a, b):
            cur = a
            total = 0
            for i in range(19 - 1, -1, -1):
                if up[cur][i] <= b:
                    total += right_total[cur][i]
                    cur = up[cur][i]
            total += arr[cur] * (b - cur + 1)
            return left_mud[a] + total - arr[a]
        pref = [0] * sz

        def fun2(l, r, opt_l, opt_r):
            if l > r:
                return
            mid = (l + r) // 2
            ans = float('inf')
            res2 = -1

            for X in range(opt_l, min(mid, opt_r) + 1):
                cost = fun(X, mid)
                if cost < ans:
                    ans = cost
                    res2 = X
            pref[mid] = ans
            fun2(l, mid - 1, opt_l, res2)
            fun2(mid + 1, r, res2, opt_r)

        fun2(0, sz - 1, 0, sz - 1)
        return pref

    pref = pf(height_limit)
    rev_pref = pf(height_limit[::-1]) 
    mx_water = 0
    for K in range(n + 1):
        left_mud = pref[K - 1] if K > 0 else 0
        right_mud = rev_pref[n - 1 - K] if K < n else 0 
        water = n * h - (left_mud + right_mud)
        if water > mx_water:
            mx_water = water 
    print(mx_water)
    pass



# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
