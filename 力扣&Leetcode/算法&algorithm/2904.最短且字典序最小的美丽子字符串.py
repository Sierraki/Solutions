class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
            wl=cur=left=0
            a_s=int(s)
            ss=[int(i) for i in s]
            if sum(ss)<k:
                return("")
            else:
                # print(s)
                for idx,i in enumerate(s):
                    cur+=int(i)
                    wl+=1
                    while cur==k:
                        t=int(s[idx+1-wl:idx+1])
                        cur-=int(s[left])
                        left+=1
                        wl-=1
                        a_s=min(t,a_s)
            return(str(a_s))

