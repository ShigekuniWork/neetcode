class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i: int):
            if i in memo:
                return memo[i]
            last_index = len(nums) - 1
            if i == last_index:
                return True
            if nums[i] == 0:
                return False

            end = min(last_index, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)