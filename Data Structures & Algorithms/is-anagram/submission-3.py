class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        I'd approach this problem using a hash map.
        Iterate through both strings to store the count of each character in hash maps.
        Then I return the result by comparing the hash map of s to the hash map of t.
        """
        # If both lengths of each string are different, return False
        if len(s) != len(t):
            return False
        
        # Initialize s_map and t_map using defaultdict(int)
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        # Start loop, i over length of string
        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        
        # Check whether both hash maps have same items
        return s_map == t_map
        """
        Time complexity is O(n): this approach uses a single loop
        Space complexity is O(n): this approach uses hash maps based on the string length
        """