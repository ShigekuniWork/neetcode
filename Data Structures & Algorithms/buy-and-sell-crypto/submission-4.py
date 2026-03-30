class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        I'd approach this problem to solve by iterateing and updating max profit and sell day each loop. 
        """
        # Assign 0 to reponse
        response = 0

        # Assign price of first day to min_buy_price
        min_buy_price = prices[0]

        # Loop start, price over prices
        for price in prices:
            # Calucrate current price with even min buy price, then assign the result to min_buy_price
            min_buy_price = min(min_buy_price, price)
            # Compare and update response
            response = max(response, price - min_buy_price)
        
        return response
        """
        Time complexity is O(n) because this approach uses single loop.
        Space complexity is O(1)
        """