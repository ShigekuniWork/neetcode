import "slices"

func isHappy(n int) bool {
	unHappyNumbers := []int{}

	for n != 1 {
		nextNumber := 0
		for n != 0 {
			digit := n % 10
			n = n / 10
			nextNumber += digit * digit
		}
		if slices.Contains(unHappyNumbers, nextNumber) {
			return false
		}
		n = nextNumber
		unHappyNumbers = append(unHappyNumbers, n)
	}

	return true
}