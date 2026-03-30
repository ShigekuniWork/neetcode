from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        min_cost = [INF] * n
        min_cost[src] = 0
        
        for _ in range(k + 1): 
            min_cost_next = min_cost.copy()
            
            for source, destination, price in flights:
                if min_cost[source] != INF:
                    current_cost = min_cost[source] + price

                    min_cost_next[destination] = min(min_cost_next[destination], current_cost)

            min_cost = min_cost_next

        final_price = min_cost[dst]
        
        return int(final_price) if final_price != INF else -1