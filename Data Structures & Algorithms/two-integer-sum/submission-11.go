func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i, n := range nums {
        diff := target - n
        if pair, found := seen[diff]; found {
            return []int{pair, i}
        }
        seen[n] = i
    }
    return []int{}
}
