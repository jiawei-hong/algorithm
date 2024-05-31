func isAnagram(s string, t string) bool {
	count := make(map[rune]int)

	for _, v := range s {
		count[v]++
	}

	for _, v := range t {
		count[v]--
	}

	for _, v := range count {
		if v != 0 {
			return false
		}
	}

	return true
}