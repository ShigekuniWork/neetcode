class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy_price = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_buy_price)
            min_buy_price = min(min_buy_price, prices[i])

        return profit