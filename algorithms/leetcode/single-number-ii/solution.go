func singleNumber(nums []int) int {
	record := map[int]int{}

	for _, num := range nums {
		record[num]++
	}

	for k, v := range record {
		if v == 1 {
			return k
		}
	}

	return 0
}