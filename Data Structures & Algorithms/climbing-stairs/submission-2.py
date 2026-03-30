class Solution:
    def climbStairs(self, n: int) -> int:
        """
        I'd approach this problem by using dynamic programing with two pointer.
        First, I prepare previous pointer and current pointer to track ever steps.
        Seconde, I update each pointer value, previous pointer over current pointer,
        current pointer over previous counter
        """
        # Arrange 1 to cur and prev
        cur, prev = 1, 1

        # star loop, i over n-1 index
        for i in range(n-1):
            temp = cur
            cur += prev
            prev = temp
        
        return cur
        """
        So this approach is one liner, time complexity is O(n).
        So no new memory other than valiable, space complexity is O(1)
        """