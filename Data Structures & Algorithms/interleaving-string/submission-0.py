class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        queue = {(0, 0)}

        for char in s3:
            next_queue = set()
            
            for i, j in queue:
                if i < len(s1) and s1[i] == char:
                    next_queue.add((i + 1, j))

                if j < len(s2) and s2[j] == char:
                    next_queue.add((i, j + 1))
            
            if not next_queue:
                return False
                
            queue = next_queue

        return True