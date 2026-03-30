class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []

        def dfs(idx, paths):
            response.append(paths.copy())

            for i in range(idx, len(nums)):
                paths.append(nums[i])
                dfs(i + 1, paths)
                paths.pop()

        dfs(0, [])
        return response