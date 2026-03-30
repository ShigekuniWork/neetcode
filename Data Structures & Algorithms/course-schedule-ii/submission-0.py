class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)

            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        if len(result) == numCourses:
            return result
        else:
            return []

