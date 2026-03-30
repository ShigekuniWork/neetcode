class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if end <= len(s) and s[i:end] == word:
                    dp[i] = dp[end]
                if dp[i]:
                    break
        
        return dp[0]