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

	xmasCounter := 0

	countXMAS(inputParsed, &xmasCounter)
	fmt.Println("XMAS Counter: ", xmasCounter)
}

func countXMAS(inputParsed []string, xmasCounter *int) {
	for indexX, line := range inputParsed {
		for indexJ, letter := range line {
			if letter == 'A' &&
				indexJ+1 < len(line) &&
				indexJ-1 >= 0 &&
				indexX+1 < len(inputParsed) &&
				indexX-1 >= 0 {

				aboveLeft := inputParsed[indexX-1][indexJ-1]
				belowRight := inputParsed[indexX+1][indexJ+1]
				aboveRight := inputParsed[indexX-1][indexJ+1]
				belowLeft := inputParsed[indexX+1][indexJ-1]

				if (aboveLeft == 'M' && belowRight == 'S' && aboveRight == 'S' && belowLeft == 'M') ||
					(aboveLeft == 'M' && belowRight == 'S' && aboveRight == 'M' && belowLeft == 'S') ||
					(aboveLeft == 'S' && belowRight == 'M' && aboveRight == 'S' && belowLeft == 'M') ||
					(aboveLeft == 'S' && belowRight == 'M' && aboveRight == 'M' && belowLeft == 'S') {
					*xmasCounter++
				}
			}
		}
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
