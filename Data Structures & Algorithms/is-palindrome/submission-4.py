class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        I'd approach this problem using two pointers.
        Iterate through the string while left pointer is less than right pointer.
        I compare the value of left pointer to the value of right pointer 
        after converting to lower case.
        If current character is neither alphabet nor number, move pointer forward to next.
        """
        # Assign 0 and last index of s to left, right
        left = 0
        right = len(s) - 1

        # Loop continues while left less than right
        while left < right:
            # Check whether current value is alphabet or number
            while left < right and not s[left].isalnum():
                left += 1

            # Check whether the right pointer as well
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare left value to right value after converting to lower case
            if s[left].lower() != s[right].lower():
                return False
            
            # Update range
            left += 1
            right -= 1
        
        return True
        """
        Time complexity is O(n)
        Space complexity is O(1)
        """