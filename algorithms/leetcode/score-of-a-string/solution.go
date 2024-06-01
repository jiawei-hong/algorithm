import "math"

func scoreOfString(s string) int {
	n := len(s) - 1
	answer := 0

	for i := range n {
		answer += int(math.Abs(float64(byte(s[i])) - float64(byte(s[i+1]))))
	}

	return answer
}
