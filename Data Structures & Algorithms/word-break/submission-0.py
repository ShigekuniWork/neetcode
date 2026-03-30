class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        max_len = max(map(len, words)) if words else 0
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            end = min(n, i + max_len)
            for j in range(i+1, end+1):
                if s[i:j] in words:
                    dp[j] = True
                    if dp[n]:
                        return True
        return dp[n]
