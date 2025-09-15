class Solution:
    def reformatDate(self, date: str) -> str:
        mo = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        res = dict(zip(mo, [i for i in range(1, 13)]))
        ans = date.split()
        y = ans[-1]
        m = str(res[ans[-2]]).zfill(2)
        d = "".join([str(i) for i in ans[0] if i.isdigit()]).zfill(2)
        return f"{y}-{m}-{d}"
