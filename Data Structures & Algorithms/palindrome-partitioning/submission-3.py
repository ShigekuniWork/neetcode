class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length -1
                dp[start][end] = (
                    s[start] == s[end] and 
                    (start + 1 > (end - 1) or 
                    dp[start + 1][end - 1])
                    )
        
        res, part = [], []
        def dfs(start):
            if start >= len(s):
                res.append(part.copy())
                return
            for end in range(start, len(s)):
                if dp[start][end]:
                    part.append(s[start : end + 1])
                    dfs(end + 1)
                    part.pop()
        
        dfs(0)
        return res
