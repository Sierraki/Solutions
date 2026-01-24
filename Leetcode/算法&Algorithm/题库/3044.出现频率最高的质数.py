class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cnt = Counter()
        for i in range(m):
            for j in range(n):
                # 水平 -->
                cur = [mat[i][j]]
                a, b = i, j + 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        b += 1
                    else:
                        break

                # <--
                cur = [mat[i][j]]
                a, b = i, j - 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        b -= 1
                    else:
                        break
                # 左上
                cur = [mat[i][j]]
                a, b = i - 1, j - 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        b -= 1
                        a -= 1
                    else:
                        break
                # 左下
                cur = [mat[i][j]]
                a, b = i + 1, j - 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        b -= 1
                        a += 1
                    else:
                        break
                # 右上
                cur = [mat[i][j]]
                a, b = i - 1, j + 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        a -= 1
                        b += 1

                    else:
                        break
                # 右下
                cur = [mat[i][j]]
                a, b = i + 1, j + 1
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1
                        b += 1
                        a += 1
                    else:
                        break
                # 下
                cur = [mat[i][j]]
                a, b = i + 1, j
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1

                        a += 1
                    else:
                        break
                # 上
                cur = [mat[i][j]]
                a, b = i - 1, j
                while 0 <= a < m and 0 <= b < n:
                    cur.append(mat[a][b])
                    if int("".join(map(str, cur))) > 10:
                        cnt[int("".join(map(str, cur)))] += 1

                        a -= 1
                    else:
                        break

        def fun(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        ans = -1
        mx_cnt = 0
        for i, j in cnt.items():
            print(i, j)
            if fun(i):
                if j > mx_cnt:
                    mx_cnt = j
                    ans = i
                elif j == mx_cnt:
                    ans = max(ans, i)
        return ans
