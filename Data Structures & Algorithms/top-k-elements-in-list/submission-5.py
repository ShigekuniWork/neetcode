class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        I would apprach this problem by using bucket sorting.
        First, count up the word number of appearences, sotre the results to hash map.
        Second, sort by hash map items.value() and get frequent elements 
        """
        # Assign the empty list to valiable 'response'
        response = []
        # Assign the empty hash map to valiable 'elemnts_count'
        elements_count = {}

        # Start loop, iterate nums
        for n in nums:
            # If the condition is True, add 1 to the count.
            if n in elements_count:
                elements_count[n] += 1
            # If the condition is False, assign 1 to the element value.
            else:
                elements_count[n] = 1
        
        # Sort by flequency and assign ot the response
        sorted_map = sorted(elements_count.items(), key = lambda x: x[1], reverse=True)
        for item in sorted_map:
            if len(response) < k:
                response.append(item[0])
        
        return response

        """
        This approach is count word number of appearences, So need itrate O(n) and 
        O(m) times when sorted hash map.
        So, O(n+m) times
        We need O(n+m) becouase hash map and reponse. 
        """
