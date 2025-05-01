
class Solution:
    def isValid(self, s: str) -> bool:
            s = [i for i in s]
            al = {"[": "]", "(": ")", "{": "}"}
            ar = {"]": "[", ")": "(", "}": "{"}

            # 最晚出现的左括号最先匹配
            # 先出现的左括号后匹配

            left=[]

            st=True
            n=len(s)
            if n%2!=0:
                return(False)
            else:
                for i in s:
                    if i in al:
                        left.append(i)
                    else:
                        if not left or ar[i]!=left[-1]:
                            st=False
                            break
                        else:
                            left.pop(-1)
                if left:
                    st=False
                        
            return(st)