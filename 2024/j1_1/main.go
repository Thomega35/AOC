package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")

	var leftList []int
	var rightList []int

	// Parse the input
	for _, line := range inputParsed {
		leftValue, err1 := strconv.Atoi(line[0])
		if err1 != nil {
			fmt.Println("Error parsing integer:", err1)
			return
		}
		rightValue, err2 := strconv.Atoi(line[1])
		if err2 != nil {
			fmt.Println("Error parsing integer:", err2)
			return
		}
		leftList = append(leftList, leftValue)
		rightList = append(rightList, rightValue)
	}

	// Sort both lists
	sort.Ints(leftList)
	sort.Ints(rightList)

	totalDistance := 0

	// Calculate the total distance
	for i := range leftList {
		distance := abs(leftList[i] - rightList[i])
		totalDistance += distance
	}

	fmt.Printf("The total distance between the lists is: %d\n", totalDistance)
	defer f.Close()
}

func mustOpenFile(filename string) (*os.File, [][]string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := [][]string{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words
		lines := strings.Split(rawText, "\n")
		for _, line := range lines {
			words := strings.Fields(line)
			inputParsed = append(inputParsed, words)
		}

	}
	return f, inputParsed
}

// Helper function to calculate the absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
