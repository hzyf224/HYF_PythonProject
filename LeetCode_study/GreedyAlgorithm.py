"""
    # 贪心算法
    假设你有几种不同面额的硬币，比如：1 元、5 元、10 元，如何用最少的硬币数来凑出指定的金额。
"""


def coin_change(coins, amount):
    # 按照硬币面额从大到小排序
    coins.sort(reverse=True)

    # 统计所需硬币的数量
    total_coins = 0

    # 逐个处理硬币面值
    for coin in coins:
        if amount == 0:
            break
        # 计算当前硬币需要多少个
        num_coins = amount // coin
        total_coins += num_coins
        # 更新剩余金额
        amount -= num_coins * coin

    # 如果最后剩余金额为0，说明能够成功凑齐
    if amount == 0:
        return total_coins
    else:
        return -1


coins_test = [1, 5, 10, 20]
amount_test = 57
result = coin_change(coins_test, amount_test)
if result != -1:
    print(f"最少需要{result}枚硬币来凑齐{amount_test}")
else:
    print(f"无法凑齐{amount_test}")
