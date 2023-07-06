func minSubArrayLen(target int, nums []int) int {
	l := 0
	cur := 0
	res := math.MaxInt32

	for r := 0; r < len(nums); r++ {
		cur += nums[r]

		for cur >= target {
			res = min(res, r-l+1)
			cur -= nums[l]
			l++
		}
	}

	if res != math.MaxInt32 {
		return res
	}

	return 0
}

func min(i, j int) int {
	if i > j {
		return j
	}

	return i
}