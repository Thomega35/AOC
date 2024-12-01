// open j1.txt
package main

import (
	"fmt"
)

func main() {
	f, inputParsed := mustOpenFile("j1.txt")

	for _, line := range inputParsed {
		for _, word := range line {
			fmt.Print(word)
			fmt.Print(" / ")
		}
		fmt.Println()
	}

	defer f.Close()
}
