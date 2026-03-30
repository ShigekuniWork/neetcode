class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        I'll approach this problem by iterating through the prices and updating the max profit each iteration. 
        """
        # Assign 0 to response
        response = 0

        # Assign price of first day to min_buy_price
        min_buy_price = prices[0]

        # Loop through each price in prices
        for price in prices:
            # Calculate and update min_buy_price with the minimum of current min_buy_price and price
            min_buy_price = min(min_buy_price, price)
            # Compare current profit with previous max profit and update response
            response = max(response, price - min_buy_price)
        
        return response
        """
        Time complexity is O(n) because this approach uses a single loop.
        Space complexity is O(1)
        """