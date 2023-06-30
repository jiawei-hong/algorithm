func removeElement(nums []int, val int) int {
    cnt := 0

    for i, num := range nums {
        if num != val {
            nums[cnt] = nums[i]
            cnt++
        }
    }

    return cnt
}