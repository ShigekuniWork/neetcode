class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {
            "}": "{",
            "]": "[",
            ")" : "(",
        }

        for c in s:
            if c in pair:
                if not stack or pair[c] != stack.pop():
                    return False
            else:
                stack.append(c)


        return not stack

