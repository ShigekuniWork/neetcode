class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (right - left < 3 or dp[left+1][right-1]):
                    dp[left][right] = True
                    res += 1
        
        return res