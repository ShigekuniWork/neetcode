class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length <= 2 or dp[start+1][end-1]:
                        dp[start][end] = True
        
        def backtrack(start):
            if start == n:
                res.append(path.copy())
            
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()

        backtrack(0)
        return res