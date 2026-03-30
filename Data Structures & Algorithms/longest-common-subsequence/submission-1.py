class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for col in range(len(text1) -1, -1, -1):
            prev_diag = 0
            for row in range(len(text2) -1, -1, -1):
                below = dp[row]
                if text1[col] == text2[row]:
                    dp[row] = 1 + prev_diag
                else:
                    dp[row] = max(below, dp[row + 1])
                
                prev_diag = below
        
        return dp[0]
