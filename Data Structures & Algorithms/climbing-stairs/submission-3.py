class Solution:
    def climbStairs(self, n: int) -> int:
        """
        I'd approach this problem by using dynamic programing with roling pointer.
        This problem is similar to the Fibonacci sequence. the number of ways to 
        reach step i equals the sum of the to reach step(i-1) and (i-2)
        I'll use two pinter to represent theses status.
        """
        # Assign 1 to prev and cur to represent first status
        prev, cur = 1, 1

        # Iterate n-1 times, updating the two pointers each round
        for _ in range(n-1):
            temp = cur
            # update cur, f(i-1) + f(i-2)
            cur += prev
            # update prev, f(i-1)
            prev = temp

        return cur

        """
        The tiem complexity is O(n) beacuse we iterate once for each loop
        The space complexity si O(1) since only two valiables are used.
        """