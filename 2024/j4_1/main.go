package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	defer f.Close()

	reversedYInputParsed := reverseTableY(inputParsed)
	reversedXInputParsed := reverseTableX(inputParsed)
	reversedYXInputParsed := reverseTableX(reversedYInputParsed)

	xmasCounter := 0

	countInlineXMAS(inputParsed, &xmasCounter)
	fmt.Println("XMAS Inline Counter: ", xmasCounter)
	countInlineXMAS(reversedXInputParsed, &xmasCounter)
	fmt.Println("XMAS Reverse Inline Counter: ", xmasCounter)
	countVertXMAS(inputParsed, &xmasCounter)
	fmt.Println("XMAS Vert Counter: ", xmasCounter)
	countVertXMAS(reversedYInputParsed, &xmasCounter)
	fmt.Println("XMAS Reverse Vert Counter: ", xmasCounter)
	countDiagonalDownXMAS(inputParsed, &xmasCounter)
	fmt.Println("XMAS Diagonal Down Counter: ", xmasCounter)
	countDiagonalDownXMAS(reversedXInputParsed, &xmasCounter)
	fmt.Println("XMAS Diagonal Up Counter: ", xmasCounter)
	countDiagonalDownXMAS(reversedYInputParsed, &xmasCounter)
	fmt.Println("XMAS Diagonal Down Reverse Counter: ", xmasCounter)
	countDiagonalDownXMAS(reversedYXInputParsed, &xmasCounter)
	fmt.Println("XMAS Diagonal Up Reverse Counter: ", xmasCounter)
}

func reverseTableY(inputParsed []string) []string {
	reversedYInputParsed := []string{}
	for i := len(inputParsed) - 1; i >= 0; i-- {
		reversedYInputParsed = append(reversedYInputParsed, inputParsed[i])
	}
	return reversedYInputParsed
}

func reverseTableX(inputParsed []string) []string {
	reversedXInputParsed := []string{}
	for _, line := range inputParsed {
		reversedLine := ""
		for i := len(line) - 1; i >= 0; i-- {
			reversedLine += string(line[i])
		}
		reversedXInputParsed = append(reversedXInputParsed, reversedLine)
	}
	return reversedXInputParsed
}

func countInlineXMAS(inputParsed []string, xmasCounter *int) {
	for _, line := range inputParsed {
		x, m, a := false, false, false
		for _, letter := range line {
			processXmasLetter(&x, &m, &a, letter, xmasCounter)
		}
	}
}

func countVertXMAS(inputParsed []string, xmasCounter *int) {
	for i := 0; i < len(inputParsed[0]); i++ {
		x, m, a := false, false, false
		for _, line := range inputParsed {
			letter := rune(line[i])
			processXmasLetter(&x, &m, &a, letter, xmasCounter)
		}
	}
}

func countDiagonalDownXMAS(inputParsed []string, xmasCounter *int) {
	for i := 0; i < len(inputParsed)+len(inputParsed[0]); i++ {
		x, m, a := false, false, false
		for j := 0; j < len(inputParsed); j++ {
			if i-j < len(inputParsed[0]) && i-j >= 0 {
				letter := rune(inputParsed[j][i-j])
				processXmasLetter(&x, &m, &a, letter, xmasCounter)
			}
		}
	}
}

func processXmasLetter(x, m, a *bool, letter rune, xmasCounter *int) {
	switch {
	case !*x && letter == 'X':
		*x = true
	case *x && !*m && letter == 'M':
		*m = true
	case *x && *m && !*a && letter == 'A':
		*a = true
	case *x && *m && *a && letter == 'S':
		*x, *m, *a = false, false, false
		(*xmasCounter)++
	default:
		*x, *m, *a = letter == 'X', false, false
	}
}

func mustOpenFile(filename string) (*os.File, []string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := []string{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words
		inputParsed = append(inputParsed, strings.Split(rawText, "\n")...)

	}
	return f, inputParsed
}
