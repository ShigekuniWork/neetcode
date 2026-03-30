func isHappy(n int) bool {
	slow, fast := n, sumOfSquares(n)
	power, count := 1, 1

	for slow != fast {
		if power == count {
			slow = fast
			power *= 2
			count = 0
		}
		fast = sumOfSquares(fast)
		count++
	}
	return fast == 1
}

func sumOfSquares(n int) int {
	result := 0
	for n > 0 {
		digit := n % 10
		result += digit * digit
		n /= 10
	}
	return result
}
