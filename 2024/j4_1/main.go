package main

import (
	"fmt"
)

func main() {
	f, inputParsed := mustOpenFile("test.txt")
	var xmasCounter *int = new(int)
	*xmasCounter = 0
	var x *bool = new(bool)
	var m *bool = new(bool)
	var a *bool = new(bool)
	// Inline XMAS
	countInlineXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Inline Counter: ", *xmasCounter)
	countReverseInlineXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS REverse Inline Counter: ", *xmasCounter)
	countVertXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Vert Counter: ", *xmasCounter)
	countReverseVertXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Reverse Vert Counter: ", *xmasCounter)
	countDiagonalDownXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Diagonal Down Counter: ", *xmasCounter)
	countDiagonalDownReverseXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Diagonal Down Reverse Counter: ", *xmasCounter)
	countDiagonalUpXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Diagonal Up Counter: ", *xmasCounter)
	countDiagonalUpReverseXMAS(inputParsed, xmasCounter, x, m, a)
	fmt.Println("XMAS Diagonal Up Reverse Counter: ", *xmasCounter)

	defer f.Close()
}

func countInlineXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	for _, line := range inputParsed {
		// Process each line here
		*x = false
		*m = false
		*a = false
		for _, letter := range line {
			processXmasLetter(x, m, a, letter, xmasCounter)
		}
	}
}

func countReverseInlineXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	for _, line := range inputParsed {
		// Process each line here
		*x = false
		*m = false
		*a = false
		for i := len(line) - 1; i >= 0; i-- {
			letter := rune(line[i])
			processXmasLetter(x, m, a, letter, xmasCounter)
		}
	}
}

func countVertXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	for i := 0; i < len(inputParsed[0]); i++ {
		// Process each line here
		*x = false
		*m = false
		*a = false
		for _, line := range inputParsed {
			letter := rune(line[i])
			processXmasLetter(x, m, a, letter, xmasCounter)
		}
	}
}

func countReverseVertXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	for i := 0; i < len(inputParsed[0]); i++ {
		// Process each line here
		*x = false
		*m = false
		*a = false
		for j := len(inputParsed) - 1; j >= 0; j-- {
			letter := rune(inputParsed[j][i])
			processXmasLetter(x, m, a, letter, xmasCounter)
		}
	}
}

func countDiagonalDownXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	// Process each line here
	for i := 0; i < len(inputParsed)+len(inputParsed[0]); i++ {
		*x = false
		*m = false
		*a = false
		for j := 0; j < len(inputParsed); j++ {
			if i-j < len(inputParsed[0]) && i-j >= 0 {
				letter := rune(inputParsed[j][i-j])
				processXmasLetter(x, m, a, letter, xmasCounter)
			}
		}
	}
}

func countDiagonalDownReverseXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	// Process each line here
	for i := len(inputParsed[0]) + len(inputParsed) - 1; i >= 0; i-- {
		*x = false
		*m = false
		*a = false
		for j := 0; j < len(inputParsed); j++ {
			if i-j < len(inputParsed[0]) && i-j >= 0 {
				letter := rune(inputParsed[j][i-j])
				processXmasLetter(x, m, a, letter, xmasCounter)
			}
		}
	}
}

func countDiagonalUpXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	// Process each line here
	for i := 0; i < len(inputParsed)+len(inputParsed[0]); i++ {
		*x = false
		*m = false
		*a = false
		for j := 0; j < len(inputParsed); j++ {
			if i-j < len(inputParsed[0]) && i-j >= 0 {
				letter := rune(inputParsed[len(inputParsed)-1-j][i-j])
				processXmasLetter(x, m, a, letter, xmasCounter)
			}
		}
	}
}

func countDiagonalUpReverseXMAS(inputParsed []string, xmasCounter *int, x *bool, m *bool, a *bool) {
	// Process each line here
	for i := len(inputParsed[0]) + len(inputParsed) - 1; i >= 0; i-- {
		*x = false
		*m = false
		*a = false
		for j := 0; j < len(inputParsed); j++ {
			if i-j < len(inputParsed[0]) && i-j >= 0 {
				letter := rune(inputParsed[len(inputParsed)-1-j][i-j])
				processXmasLetter(x, m, a, letter, xmasCounter)
			}
		}
	}
}

func processXmasLetter(x, m, a *bool, letter rune, xmasCounter *int) {
	// Process XMAS letter here
	if !*x {
		if letter == 'X' {
			*x = true
		}
	} else if !*m {
		if letter == 'M' {
			*m = true
		} else if letter != 'X' {
			*x = false
		}
	} else if !*a {
		if letter == 'A' {
			*a = true
		} else if letter == 'X' {
			*m = false
		} else {
			*x = false
			*m = false
		}
	} else {
		if letter == 'S' {
			*xmasCounter++
			*x = false
			*m = false
			*a = false
		} else if letter == 'X' {
			*m = false
			*a = false
		} else {
			*x = false
			*m = false
			*a = false
		}
	}
}
