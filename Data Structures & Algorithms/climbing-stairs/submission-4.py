class Solution:
    def climbStairs(self, n: int) -> int:
        """
        I'd approach this problem by using dynamic programming with two rolling pointers.
        This problem is similar to the Fibonacci sequence: the number of ways to reach
        step i equals the sum of the ways to reach steps (i - 1) and (i - 2).
        I'll use two pointers to represent these states and update them iteratively.
        """

        # Assign 1 to both 'prev' and 'cur' to represent the base cases
        prev, cur = 1, 1

        # Iterate (n - 1) times, updating the two pointers each round
        for _ in range(n - 1):
            temp = cur
            # Update 'cur' with f(i) = f(i - 1) + f(i - 2)
            cur += prev
            # Update 'prev' to the previous 'cur'
            prev = temp

        return cur

        """
        The time complexity is O(n) because we iterate once for each step.
        The space complexity is O(1) since only two variables are used.
        """
