func longestSubarray(nums []int) int {
	zeroCount := 0
	longestWindow := 0
	start := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			zeroCount++
		}

		for zeroCount > 1 {
			if nums[start] == 0 {
				zeroCount--
			}
			start++
		}

		longestWindow = max(longestWindow, i-start)
	}

	return longestWindow
}

func max(i, j int) int {
	if i > j {
		return i
	}

	return j
}