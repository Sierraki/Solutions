class Solution:
    def isNumber(self, s: str) -> bool:
        # 定义状态转移表
        # 每个状态是一个字典，Key 是输入类型，Value 是跳转后的状态
        states = [
            {"sign": 1, "digit": 2, "dot": 4},  # 0. start
            {"digit": 2, "dot": 4},  # 1. sign
            {"digit": 2, "dot": 3, "exp": 6},  # 2. int
            {"digit": 5, "exp": 6},  # 3. dot (left has digits)
            {"digit": 5},  # 4. dot (left no digits)
            {"digit": 5, "exp": 6},  # 5. fraction
            {"sign": 7, "digit": 8},  # 6. exp
            {"digit": 8},  # 7. exp_sign
            {"digit": 8},  # 8. exp_int
        ]
        cur_state = 0
        for char in s:
            # 1. 判定当前输入类型
            if char.isdigit():
                typ = "digit"
            elif char in "+-":
                typ = "sign"
            elif char in "eE":
                typ = "exp"
            elif char == ".":
                typ = "dot"
            else:
                return False  # 出现非法字符直接返回
            # 2. 状态跳转
            if typ not in states[cur_state]:
                return False  # 当前状态不能接受这种输入，说明不合法
            cur_state = states[cur_state][typ]
        # 3. 判断最终停留的状态是否是“合法结尾”
        # 合法的结尾状态：整数(2)、有左数字的小数点(3)、小数(5)、指数整数(8)
        return cur_state in [2, 3, 5, 8]
