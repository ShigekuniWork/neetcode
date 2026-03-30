class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        I'd approach to solev this ploblem by using tow pointer.
        Itrate though the list while left poiter is less than right pointer.
        I compre the value of left pointer to the value of right pointer 
        after comverting slower case.
        If current pointer is nether alphabet or number, pointer forwards to next.
        """
        # Assign 0 and last index of s to left, right
        left = 0
        right = len(s) - 1

        # Loop continue while left less than right
        while left < right:
            # Check whtere current value is alhabet or number
            while left < right and not s[left].isalnum():
                left += 1

            # Check whter the right pointer as well
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare left value to right value after comverting lower caces
            if s[left].lower() != s[right].lower():
                return False
            
            # update range
            left += 1
            right -= 1
        
        return True
        """
        Time complexity is O(n)
        Space complexity is O(1)
        """

        