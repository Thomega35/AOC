package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	defer f.Close()

	sumTestVal := int64(0)

	for _, line := range inputParsed {
		testVal := line[0]
		if isCalculable(testVal, line[2:], line[1]) {
			sumTestVal += testVal
		}
	}
	fmt.Println("Sum of testVal:", sumTestVal)
}

func mustOpenFile(filename string) (*os.File, [][]int64) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := [][]int64{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words
		lines := strings.Split(rawText, "\n")
		for _, line := range lines {
			words := strings.FieldsFunc(line, Split)
			numbers := []int64{}
			for _, word := range words {
				num, err := strconv.ParseInt(word, 10, 64)
				if err != nil {
					fmt.Println("Error converting string to int:", err)
					return nil, nil
				}
				numbers = append(numbers, num)
			}
			inputParsed = append(inputParsed, numbers)
		}

	}
	return f, inputParsed
}

func Split(r rune) bool {
	return r == ':' || r == ' '
}

func isCalculable(testVal int64, numbers []int64, currentSum int64) bool {
	if len(numbers) == 0 {
		return currentSum == testVal
	}
	concatVal, err := strconv.ParseInt((strconv.FormatInt(currentSum, 10) + strconv.FormatInt(numbers[0], 10)), 10, 64)
	if err != nil {
		return false
	}
	return isCalculable(testVal, numbers[1:], currentSum+numbers[0]) ||
		isCalculable(testVal, numbers[1:], currentSum*numbers[0]) ||
		isCalculable(testVal, numbers[1:], concatVal)
}
