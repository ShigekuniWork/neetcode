class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'd approach to solve this problem by using hash map.
        I store count that if the number is selected to hash map.
        So I assign current number, count that previous number and next number 
        value of hash map.
        Then I update number of range that start point and endpoint of sequence number.
        """
        # Assign 0 to response
        response = 0

        # Initialize hash map by using defaultdict(int)
        count_map = defaultdict(int)

        # Start loop, n over nums:
        for n in nums:
            # Check wehter n in nums
            if not count_map[n]:
                # If the condition is True,
                # Update count of current nums based on count of previous num and 
                # next num.
                count_map[n] = count_map[n-1] + count_map[n+1] + 1
                # Update range of sequence numbers
                count_map[n - count_map[n-1]] = count_map[n]
                count_map[n + count_map[n+1]] = count_map[n]
                # update longest sequence
                response = max(response, count_map[n])

        return response
        """
        Time complexity is O(n) because this approach takes one liner.
        Space complexity is O(n) because I used hash map for counting.
        """ 