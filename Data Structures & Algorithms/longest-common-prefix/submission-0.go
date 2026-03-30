func longestCommonPrefix(strs []string) string {
	for i := range len(strs[0]) {
		for j := 1; j < len(strs); j++ {
			cur := strs[j]
			if i == len(cur) || cur[i] != strs[0][i]{
				return cur[:i]
			}
		}
	}
	return strs[0]
}

