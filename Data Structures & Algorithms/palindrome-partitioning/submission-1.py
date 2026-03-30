class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        
        # DPテーブルの作成 (dp[i][j] は s[i:j+1] が回文かどうか)
        # 事前計算: O(N^2)
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # 2文字以下、または内側が回文ならTrue
                    if length <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        
        # バックトラッキング: O(N * 2^N) だが判定定数が軽い
        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                # DPテーブルを参照してO(1)で判定
                if dp[start][end]:
                    path.append(s[start : end + 1])
                    backtrack(end + 1)
                    path.pop()
                    
        backtrack(0)
        return res