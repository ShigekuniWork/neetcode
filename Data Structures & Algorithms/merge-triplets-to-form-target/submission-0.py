class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mergedTriplets = [0] * 3

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    mergedTriplets[i] = max(mergedTriplets[i], t[i])
        
        return mergedTriplets == target