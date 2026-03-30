import collections
from typing import List
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [float('inf')] * n
        dist[k - 1] = 0
        
        for _ in range(n - 1):
            relaxed = False
            for u, v, w in times:
                if dist[u - 1] != float('inf'):
                    if dist[u - 1] + w < dist[v - 1]:
                        dist[v - 1] = dist[u - 1] + w
                        relaxed = True
            
            if not relaxed:
                break

        for u, v, w in times:
            if dist[u - 1] != float('inf'):
                if dist[u - 1] + w < dist[v - 1]:
                    return -1 # 負の閉路が検出された場合

        max_dist = max(dist)
        
        return int(max_dist) if max_dist < float('inf') else -1