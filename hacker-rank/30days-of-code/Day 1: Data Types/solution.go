package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var _ = strconv.Itoa

	var i uint64 = 4
	var d float64 = 4.0
	var s string = "HackerRank "

	scanner := bufio.NewScanner(os.Stdin)

	var i2 uint64
	var d2 float64
	var s2 string

	fmt.Scanln(&i2)
	fmt.Scanln(&d2)
	scanner.Scan()
	s2 = scanner.Text()

	fmt.Println(i + i2)
	fmt.Printf("%.1f\n", d+d2)
	fmt.Println(s + s2)
}
