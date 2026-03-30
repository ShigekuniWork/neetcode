from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        I will approach this problem using the Sliding Window technique combined with a Hash Map.
        
        The strategy is to iterate through the string 's' with the 'right' pointer and maintain a count of characters in the current window.
        
        The condition for an invalid window is when:
        (Current Window Length) - (Count of the Most Frequent Character) > k
        
        If the window becomes invalid (i.e., we need more than 'k' replacements), 
        we shrink the window by moving the 'left' pointer forward and decreasing the count of the character at that position.
        
        We continuously update the maximum valid window length found so far.
        """
        # Assign a hash map (defaultdict) to store character counts
        mp = defaultdict(int)
        # Initialize the maximum valid window length (the result)
        response = 0

        # Initialize left pointer
        left = 0
        # Initailize max_count to track the highest frequency of any character ever seen in the current valid window
        max_count = 0

        # Loop starts, 'right' pointer iterates over the index of s
        for right in range(len(s)):
            # 1. Expand the window and update the current character's count
            mp[s[right]] += 1
            
            # 2. Update the maximum frequency found so far
            # This is crucial for the O(N) optimization
            max_count = max(max_count, mp[s[right]])

            # 3. Check for an invalid window and shrink it if necessary
            # The number of characters to change = (Window Length) - (Max Frequency)
            # If this number is greater than k, the window is invalid.
            while (right - left + 1) - max_count > k:
                # Shrink the window: remove the character at 'left'
                mp[s[left]] -= 1
                # Move the left pointer forward
                left += 1
            
            # 4. Update the response with the length of the current valid window
            response = max(response, right - left + 1)

        return response
        """
        Time Complexity: O(n)
        The right pointer moves 'n' times, and the left pointer moves at most 'n' times. The total number of pointer movements is O(2n), which simplifies to O(n).
        
        Space Complexity: O(m)
        'm' is the size of the alphabet or the total number of unique characters in the string (at most 26 for English uppercase letters). This is considered O(1) in the case of a fixed alphabet size.
        """