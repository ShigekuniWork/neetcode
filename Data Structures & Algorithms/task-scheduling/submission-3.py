class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]
        width = maxf - 1
        idel = width * n

        for i in range(24, -1, -1):
            idel -= min(width, count[i])
        return max(0, idel) + len(tasks)