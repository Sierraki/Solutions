# 力扣77，给n=int,k=int，求1到n的所有长度为k的组合


def combination(n=int, k=int):
    res = []

    def backtrack(start_num=int, cur_list=list):
        # 终止条件
        # 长度为k就加入res，然后终止
        if len(cur_list) == k:
            res.append(cur_list.copy())
            return
        # 剪枝优化（pruning）
        # 如果剩下的个数不够，也返回
        if n - start_num + 1 < k - len(cur_list):
            return
        # 循环
        for i in range(start_num, n + 1):
            # 从第一个数字开始
            # 加入构建层
            cur_list.append(i)
            # 进入递归循环
            backtrack(i + 1, cur_list)
            # 构建层pop一个，让下一次的循环继续加入元素，不然元素会积累
            cur_list.pop()
