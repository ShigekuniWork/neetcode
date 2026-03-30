class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        response = []
        def dfs(idex: int, cur: List[int]):
            if idex == len(nums):
                response.append(cur.copy())
                return

            for i in range(idex, len(nums)):
                cur[i], cur[idex] = cur[idex], cur[i]
                dfs(idex+1, cur)
                cur[i], cur[idex] = cur[idex], cur[i]

        dfs(0, nums)
        return response
