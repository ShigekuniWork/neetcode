class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while curr != 1:
            if curr in seen:
                return False
            seen.add(curr)

            temp = 0
            while curr:
                div, mod = divmod(curr, 10)
                temp += mod * mod
                curr = div
            curr = temp

        return True