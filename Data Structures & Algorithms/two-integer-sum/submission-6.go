func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i, n := range nums {
        diff := target - n

        if index, found := seen[diff]; found {
            return []int{index, i}
        }
        seen[n] = i
    }

    return []int{}
}
