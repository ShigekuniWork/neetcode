class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = end = 0

        def expand(left:int, right:int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right - 1

        for i in range(len(s)):
            even_s, even_e = expand(i, i+1)
            odd_s, odd_e = expand(i, i)

            if even_e - even_s > end - start:
                start, end = even_s, even_e

            if odd_e - odd_s > end - start:
                start, end = odd_s, odd_e

        return s[start:end+1]
