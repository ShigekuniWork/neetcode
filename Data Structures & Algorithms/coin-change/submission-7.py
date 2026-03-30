class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount: int):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float("INF")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        min_coins = dfs(amount)
        return -1 if min_coins >= float("INF") else min_coins