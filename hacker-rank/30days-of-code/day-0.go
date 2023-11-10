package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    fmt.Printf("Hello, World.\n")
    fmt.Println(text)
}
