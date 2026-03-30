class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for start, end in prerequisites:
            indegree[end] += 1
            adj[start].append(end)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        while q:
            end = q.popleft()
            finish += 1

            for nei in adj[end]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses