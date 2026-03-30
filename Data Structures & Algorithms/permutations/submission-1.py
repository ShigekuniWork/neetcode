class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        used = set()

        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for x in nums:
                if x in used:
                    continue
                curr.append(x)
                used.add(x)
                dfs(curr)
                curr.pop()
                used.remove(x)

        dfs([])
        return res
