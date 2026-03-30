class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count_pli(s: str, left: int, right: int):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            return res
        
        for i in range(len(s)):
            res += count_pli(s, i, i) # odd
            res += count_pli(s, i, i+1) # even

        return res