class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def maxPalindrome(left: int, right: int):
            nonlocal res

            if left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                curr = s[left:right+1]
                if len(curr) > len(res):
                    res = curr
                left -= 1
                right += 1
                maxPalindrome(left, right)

        for i in range(len(s)):
            maxPalindrome(i, i)
            maxPalindrome(i, i + 1)
        
        return res