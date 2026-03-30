class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        left = 0
        right = 0

        while left < len(s2):
            while left < len(s2) and s2[left] not in target:
                left += 1
            right = left + len(s1)
            if right > len(s2):
                return False

            cur = Counter(s2[left:right])
            if target == cur:
                return True

            left += 1
        return False