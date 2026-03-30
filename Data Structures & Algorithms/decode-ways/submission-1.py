class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        res = 0

        def dfs(index: int):
            if index in dp:
                return dp[index]
            if s[index] == "0":
                return 0
            
            res = dfs(index + 1)
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                res += dfs(index + 2)
            
            dp[index] = res
            return res
        
        return dfs(0)