func getConcatenation(nums []int) []int {
    numsLength := len(nums)

    arr := make([]int, numsLength * 2)
	for i := range(nums) {
		arr[i] = nums[i]
		arr[i + numsLength] = nums[i]
	}

	return  arr
}