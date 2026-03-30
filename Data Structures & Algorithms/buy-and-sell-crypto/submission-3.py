class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        I would approch this problem by iterating though prices
        and update minmal buy price and sell day
        """

        # Assign 0 to the valiable 'max_profit'
        max_profit = 0
        # Assing minimal buy price as first of prices to min_buy_price
        min_buy_price = prices[0]

        # loop start, price over prices
        for price in prices:
            # if price less than min_buy_price, update the price
            min_buy_price = min(min_buy_price, price)
            # if we can get profit grater than previous max_profit, update the profit
            max_profit = max(max_profit, price - min_buy_price)
        
        return max_profit