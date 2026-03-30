import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, num_cities: int, flights: List[List[int]], src: int, dst: int, max_stops: int) -> int:
        
        # グラフの構築: adjacency_list[source] = [(destination, price), ...]
        adjacency_list = [[] for _ in range(num_cities)]
        for source, destination, price in flights:
            adjacency_list[source].append((destination, price))

        INF = float("inf")
        
        # 最大許容フライト回数 (K ストップ = K+1 フライト)
        max_flights = max_stops + 1 
        
        # dist[city][flights_used]: cityに、正確にflights_used回のフライトで到達する最小コスト
        # サイズは 0 から max_flights のフライト回数をカバーする max_flights + 1 (つまり k + 2)
        dist = [[INF] * (max_flights + 1) for _ in range(num_cities)] 

        # 優先度キュー (Min Heap): (コスト, ノード, フライト回数)
        min_heap = [(0, src, 0)] 
        dist[src][0] = 0
        
        cheapest_price = INF

        while min_heap:
            current_cost, current_city, flights_used = heapq.heappop(min_heap)
            
            # 1. 目的地チェック
            if current_city == dst:
                cheapest_price = min(cheapest_price, current_cost)
                # 最小コストを記録したら、これ以上フライトを続ける必要はないため、次のノードへ
                continue
            
            # 2. 枝刈り (プルーニング) - 劣ったパスのスキップ
            # ヒープから取り出したコストが、既に記録されているより安い最小コストよりも高ければスキップ
            if current_cost > dist[current_city][flights_used]:
                continue
            
            # 3. 最大フライト回数チェック
            # 最大許容回数に達したら、これ以上フライトは使えないのでスキップ
            if flights_used == max_flights:
                continue

            # 4. 隣接ノードへの探索
            for next_city, price in adjacency_list[current_city]:
                next_cost = current_cost + price
                next_flights_used = flights_used + 1

                # 次の状態 (next_city, next_flights_used) の最小コストを更新できるかチェック
                if next_cost < dist[next_city][next_flights_used]:
                    dist[next_city][next_flights_used] = next_cost
                    heapq.heappush(min_heap, (next_cost, next_city, next_flights_used))

        return cheapest_price if cheapest_price != INF else -1
