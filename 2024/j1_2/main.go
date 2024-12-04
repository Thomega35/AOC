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

	similarityScore := 0

	// Determine map of number of occurences of each element in the right list
	rightListMap := make(map[int]int)
	for _, value := range rightList {
		rightListMap[value]++
	}

	// Calculate the similarity score
	for _, value := range leftList {
		similarityScore += rightListMap[value] * value
	}

	fmt.Printf("The similarity score is: %d\n", similarityScore)
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
