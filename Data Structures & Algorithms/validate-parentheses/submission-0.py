class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {
            "}": "{",
            "]": "[",
            ")" : "(",
        }

        for c in s:
            if c in ("]", "}", ")"):
                if not stack or pair.get(c) != stack.pop():
                    return False
            else:
                stack.append(c)


        return not stack

