from typing import List
import sys

input = [7, 1, 5, 3, 6, 4]


def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    print(min_price)

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(maxProfit(input))
