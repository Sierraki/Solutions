#!/usr/bin/env python3

import math
import sys
import time

import requests

# ================= 配置区域 =================
# 门槛分 (通常是 1600)
RATING_CUTOFF = 1600
# 勋章比例
RATIO_GUARDIAN = 0.05  # Top 5%
RATIO_KNIGHT = 0.25  # Top 25%
# ===========================================


class LC_Crawler:
    # 【修复点】：URL 必须定义在类里面，下面的 fetch_page 才能通过 LC_Crawler.URL 访问到
    URL = "https://leetcode.cn/graphql"

    HEADERS = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://leetcode.cn",
        "Referer": "https://leetcode.cn/contest/",
    }

    # 查询 globalRanking
    QUERY = r"""
        {
            globalRanking(page: PAGE_NUM) {
                totalUsers
                userPerPage
                rankingNodes {
                    currentRating
                    currentGlobalRanking
                    dataRegion
                    user {
                        username
                    }
                }
            }
        }
    """

    @staticmethod
    def fetch_page(page):
        """获取指定页码的数据"""
        retry = 0
        while retry < 3:
            try:
                payload = {
                    "operationName": None,
                    "variables": {},
                    # 简单的字符串替换，避免 JSON 序列化问题
                    "query": LC_Crawler.QUERY.replace("PAGE_NUM", str(page)),
                }

                # 这里调用 LC_Crawler.URL 以前会报错，现在修好了
                resp = requests.post(
                    LC_Crawler.URL, headers=LC_Crawler.HEADERS, json=payload, timeout=10
                )

                if resp.status_code != 200:
                    # 如果是 400 错误，可能是页码超了，不要重试直接返回 None
                    if resp.status_code == 400:
                        return None
                    raise Exception(f"HTTP {resp.status_code}")

                data = resp.json()
                if "errors" in data:
                    # 忽略非致命错误，只要有数据就行
                    if "data" in data and data["data"]:
                        pass
                    else:
                        print(
                            f"   [警告] GraphQL Error: {data['errors'][0]['message']}"
                        )

                return data["data"]["globalRanking"]
            except Exception as e:
                print(f"   [重试 {retry+1}/3] 第 {page} 页获取失败: {e}")
                retry += 1
                time.sleep(1)
        return None


def get_total_users_above_cutoff():
    """
    1. 获取全球总人数
    2. 二分查找 1600 分的截止排名
    """
    print("📡 正在连接 LeetCode 接口...")

    # 1. 先查第1页拿元数据
    first_page = LC_Crawler.fetch_page(1)
    if not first_page:
        print("❌ 无法连接服务器，请检查网络或 URL 配置。")
        sys.exit(1)

    total_users = first_page["totalUsers"]
    per_page = first_page["userPerPage"]
    total_pages = math.ceil(total_users / per_page)

    print(f"   全球参赛总人数: {total_users}")
    print(f"   正在通过二分查找锁定 {RATING_CUTOFF} 分的排名位置...")

    # 2. 二分查找 1600 分的分界线
    l, r = 1, total_pages
    cutoff_node = None

    # 进度显示优化
    last_print_len = 0

    while l <= r:
        mid = (l + r) // 2
        data = LC_Crawler.fetch_page(mid)
        if not data:
            # 网络彻底挂了
            sys.exit(1)

        nodes = data["rankingNodes"]
        if not nodes:
            # 空页，往左找
            r = mid - 1
            continue

        # 检查这一页的最高分
        top_score = float(nodes[0]["currentRating"])

        # 打印进度条效果 (覆盖上一行)
        msg = f"   🔍 扫描第 {mid} 页 | 当前分段: {top_score:.1f}"
        print(msg + " " * (last_print_len - len(msg)), end="\r")
        last_print_len = len(msg)

        if top_score < RATING_CUTOFF:
            # 这一页分数太低了，往排名靠前（页码小）的地方找
            r = mid - 1
        else:
            # 这一页分数 >= 1600
            # 检查这一页有没有 < 1600 的（即分界线是否在这一页）
            found_cutoff_here = False
            last_valid_node = None

            for node in nodes:
                if float(node["currentRating"]) >= RATING_CUTOFF:
                    last_valid_node = node
                else:
                    # 找到了第一个小于 1600 的，说明 cutoff 就是上一个
                    found_cutoff_here = True
                    break

            if found_cutoff_here:
                # 分界线就在这一页
                cutoff_node = last_valid_node
                break  # 找到了，结束循环

            # 如果这一页所有人分数都 >= 1600，说明分界线在更后面
            # 记录当前这一页最后一个作为备选，继续往后找
            cutoff_node = nodes[-1]
            l = mid + 1

    print("\n   ✅ 锁定完成！")
    return cutoff_node


def analyze_gatekeeper(rank_name, target_rank):
    """
    直接跳转到目标排名所在的页面，分析守门员
    """
    print(f"\n🔍 正在定位 {rank_name} (排名 {target_rank})...")

    # 计算页码 (每页25人)
    # 比如 排名1 -> page 1, idx 0
    # 排名 25 -> page 1, idx 24
    # 排名 26 -> page 2, idx 0
    page = (target_rank - 1) // 25 + 1
    index = (target_rank - 1) % 25

    data = LC_Crawler.fetch_page(page)
    if not data:
        print("   [错误] 无法获取该页数据")
        return

    nodes = data["rankingNodes"]

    # 1. 真正的“全球守门员”
    if index < len(nodes):
        keeper = nodes[index]
        print_user_info(f"🏆 {rank_name} 全球守门员", keeper)

        # 2. 顺便看看这一页有没有国区/美区的邻居
        nearest_cn = None
        nearest_us = None

        for node in nodes:
            region = node["dataRegion"]
            if region == "CN" and nearest_cn is None:
                nearest_cn = node
            if region == "US" and nearest_us is None:
                nearest_us = node

        print(f"   ------------------------------------------------")
        if nearest_cn:
            print_user_info(f"   [参考] 同页最近的国区用户", nearest_cn)
        else:
            print(f"   [参考] 本页 ({page}页) 无国区用户")

        if nearest_us:
            print_user_info(f"   [参考] 同页最近的美区用户", nearest_us)
        else:
            print(f"   [参考] 本页 ({page}页) 无美区用户")


def print_user_info(title, node):
    try:
        score = f"{float(node['currentRating']):.2f}"
        rank = node["currentGlobalRanking"]
        region = node["dataRegion"]
        username = node["user"]["username"]

        # 装饰图标
        flag = "🇨🇳" if region == "CN" else "🇺🇸"

        print(f"{title}:")
        print(f"      ID: {username:<18} 地区: {flag} {region}")
        print(f"      分数: {score:<18} 排名: {rank}")
    except Exception as e:
        print(f"{title}: 数据解析错误 - {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("      LeetCode 勋章分数线预测脚本 (Pro修复版)")
    print("=" * 50)

    # 1. 确定分母 (有效总人数)
    last_user = get_total_users_above_cutoff()

    if not last_user:
        print("❌ 未找到 1600 分以上的用户")
        sys.exit()

    n = int(last_user["currentGlobalRanking"])
    print(f"📊 全球 1600 分以上有效用户数: {n}")

    # 2. 计算排名阈值 (向下取整)
    rank_guardian = int(n * RATIO_GUARDIAN)
    rank_knight = int(n * RATIO_KNIGHT)

    print(f"📉 预测 Guardian (Top 5%) 排名: {rank_guardian}")
    print(f"📉 预测 Knight   (Top 25%) 排名: {rank_knight}")

    # 3. 精确抓取守门员
    analyze_gatekeeper("Guardian", rank_guardian)
    analyze_gatekeeper("Knight", rank_knight)

    print("\n" + "=" * 50)
    print("注：官方勋章结算以【全球排名】为准。")
    print("    附近的 CN/US 用户仅供参考，分数线是统一的。")
    print("=" * 50)
