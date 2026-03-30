from collections import defaultdict
import heapq
from typing import List, Set, Tuple

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        def _push_latest_tweet_to_heap(heap: list, followee_id: int, is_max_heap_mode: bool):
            if followee_id in self.tweetMap:
                index = len(self.tweetMap[followee_id]) - 1
                if index >= 0:
                    count, tweetId = self.tweetMap[followee_id][index]
                    heap_count = -count if is_max_heap_mode else count
                    heapq.heappush(heap, [heap_count, tweetId, followee_id, index - 1])
        
        followee_ids = self.followMap[userId]
        
        if len(followee_ids) >= 10:
            maxHeap = []
            
            for followeeId in followee_ids:
                _push_latest_tweet_to_heap(maxHeap, followeeId, is_max_heap_mode=True)
                
                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
            
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        
        else:
            for followeeId in followee_ids:
                _push_latest_tweet_to_heap(minHeap, followeeId, is_max_heap_mode=False)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index >= 0:
                count_next, tweetId_next = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count_next, tweetId_next, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)