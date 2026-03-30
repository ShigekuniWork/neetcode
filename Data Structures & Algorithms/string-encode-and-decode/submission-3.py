class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        
        for c in strs:
            length = len(c)
            response += f"{length}#{c}"

        return response

    def decode(self, s: str) -> List[str]:
        response = []

        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            response.append(s[left:right])
            left = right

        return response