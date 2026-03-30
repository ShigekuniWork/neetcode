func majorityElement(nums []int) int {
	response := 0
	count := 0

	for _, currentNum := range nums {
		if count == 0 {
			response = currentNum
		}

		if currentNum == response {
			count++
		} else {
			count--
		}
	}

	return response
}