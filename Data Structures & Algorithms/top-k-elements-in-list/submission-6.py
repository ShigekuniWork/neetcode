from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        The idea is to use a bucket approach.
        First, count how many times each number appears using a hash map.
        Then prepare a list of buckets, where the index represents the frequency.
        Put each number into the bucket based on how many times it appears.
        Finally, scan the buckets from the highest frequency and collect the first k numbers.
        """

        # Assign an empty hash map to store counts
        count = {}
        # Assign an empty list to store the final response
        result = []

        # Start a loop, iterate 'n' over 'nums'
        for n in nums:
            # Increase count if already exists, otherwise set to 1
            count[n] = 1 + count.get(n, 0)

        # Create buckets: index = frequency, value = list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put each number into the bucket based on its frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Scan buckets from the highest frequency to collect k elements
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                # Stop when k numbers are collected
                if len(result) == k:
                    return result

        return result

        """
        Counting happens in one scan, so O(n).
        Buckets are created in O(n).
        Collecting results also stays within O(n).
        Space is O(n) because of the hash map and buckets.
        """
