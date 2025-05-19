class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        loss = []  # cashback < cost
        profit = []  # cashback >= cost
        for cost, cashback in transactions:
            if cashback < cost:
                loss.append((cost, cashback))
            else:
                profit.append((cost, cashback))
        # 排序规则
        loss.sort(key=lambda x: x[1])  # 按 cashback 升序
        profit.sort(reverse=True)  # 按 cost 降序
        print(loss)
        print(profit)
        total = 0
        money = 0
        for cost, cashback in loss + profit:
            if money < cost:
                total += cost - money
                money = cost
            money = money - cost + cashback
        print(total)
        return total
