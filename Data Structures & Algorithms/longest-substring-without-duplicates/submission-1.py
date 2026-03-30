class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        I'll approach this problem by using sliding window.
        Iterate though the s and store the value to the hash map and update response.
        If current value is contain in the hash map, left pointer move forword next pointer with
        bigger pointer. 
        """
        # Initialze hash map and left and response
        mp = {}
        left = 0
        response = 0

        # iterate thought the index of s as right
        for right in range(len(s)):
            # Check wether the current value is ever seen
            if s[right] in mp:
                # If condition is True, Update left pointer
                left = max(mp[s[right]] + 1, left)
            
            # Assign current value to hash map
            mp[s[right]] = right
            # Update response
            response = max(response, right - left + 1)
        
        return response
        """
        Time complexity is O(n) because this approach uses single loop.
        Space comlexity is O(n) because this approach uses hash map to store ever seen value.
        """


