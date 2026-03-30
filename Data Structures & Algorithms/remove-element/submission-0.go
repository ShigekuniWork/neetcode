func removeElement(nums []int, val int) int {
	k := 0
	for i := range len(nums) {
		if nums[i] != val {
			nums[k] = nums[i]
			k += 1
		}
	}
	return k
}