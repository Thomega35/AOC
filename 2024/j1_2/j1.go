// open j1.txt
package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	f, inputParsed := mustOpenFile("j1.txt")

	leftList := []int{}
	rightList := []int{}

	// Parse the input
	for _, line := range inputParsed {
		leftValue, _ := strconv.Atoi(line[0])
		rightValue, _ := strconv.Atoi(line[1])
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
