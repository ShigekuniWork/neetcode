class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idex, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for i in range(idex, len(nums)):
                if total + nums[i] > target:
                    break
                curr.append(nums[i])
                dfs(i, curr, total + nums[i])
                curr.pop()

        dfs(0, [], 0)
        return res