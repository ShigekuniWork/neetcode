class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = []
        numbers = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for j in range(i, len(digits)):
                values = numbers[digits[j]]
                for v in values:
                    temp = curr
                    curr += v
                    dfs(j+1, curr)
                    curr = temp
        dfs(0, "")
        return res