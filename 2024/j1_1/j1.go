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

	totalDistance := 0

	// Calculate the total distance
	for i := range leftList {
		distance := abs(leftList[i] - rightList[i])
		totalDistance += distance
	}

	fmt.Printf("The total distance between the lists is: %d\n", totalDistance)
	defer f.Close()
}
