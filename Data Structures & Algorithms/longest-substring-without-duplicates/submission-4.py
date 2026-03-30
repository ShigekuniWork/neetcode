class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        mp = {}

        for right in range(len(s)):
            cur = s[right]
            if cur in mp:
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right
            res = max(res, right - left + 1)
        
        return res