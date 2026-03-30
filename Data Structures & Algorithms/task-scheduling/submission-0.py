class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        
        while maxHeap or q:
            time += 1
            
            if not maxHeap and q:
                _, next_ready_time = q[0]
                if time < next_ready_time:
                    time = next_ready_time

            while q:
                cnt, ready_time = q[0]
                
                if ready_time <= time:
                    heapq.heappush(maxHeap, cnt)
                    q.popleft()
                else:
                    break

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n + 1])
                    
        return time