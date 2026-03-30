class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [False] * n
        res = 0

        for i in range(n-1, -1, -1):
            prev = False

            for j in range(i, n):
                tmp = dp[j]

                if s[i] == s[j]:
                    dp[j] = (j - i <= 2) or prev
                else:
                    dp[j] = False

                if dp[j]:
                    res += 1

                prev = tmp

        return res
