class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(idex: int):
            if idex >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idex])
            dfs(idex + 1)
            subset.pop()
            dfs(idex + 1)
        
        dfs(0)
        return res