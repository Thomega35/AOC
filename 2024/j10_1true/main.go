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
	fmt.Println(inputParsed)

	numerInputParsed := customInputParsing(inputParsed)
	numberOfPath := calculateNumberOfPath(numerInputParsed)
	fmt.Println(numerInputParsed)
	fmt.Println(numberOfPath)
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
		lines := strings.Split(rawText, "\n")
		inputParsed = append(inputParsed, lines...)
	}
	return f, inputParsed
}

func customInputParsing(inputParsed []string) [][]int {
	result := make([][]int, len(inputParsed))
	for line := range inputParsed {
		for floorRune := range inputParsed[line] {
			numberFloorRune, _ := strconv.Atoi(string(inputParsed[line][floorRune]))
			result[line] = append(result[line], numberFloorRune)
		}
	}
	return result
}

func calculateNumberOfPath(numerInputParsed [][]int) int {
	numberOfPath := 0
	for i := 0; i < len(numerInputParsed); i++ {
		for j := 0; j < len(numerInputParsed[i]); j++ {
			if numerInputParsed[i][j] == 0 {
				currentSetOfTopReached := make(map[coordinate]bool)
				recCalculateNumberOfPath(numerInputParsed, i, j, currentSetOfTopReached)
				numberOfPath += len(currentSetOfTopReached)
			}
		}
	}
	return numberOfPath
}

// return a set of unique coordinate
func recCalculateNumberOfPath(numerInputParsed [][]int, i, j int, topReached map[coordinate]bool) {
	curerentValue := numerInputParsed[i][j]
	if curerentValue == 9 {
		topReached[coordinate{i, j}] = true
	}
	// Check four neighbor
	if i > 0 && numerInputParsed[i-1][j] == curerentValue+1 {
		recCalculateNumberOfPath(numerInputParsed, i-1, j, topReached)
	}
	if i < len(numerInputParsed)-1 && numerInputParsed[i+1][j] == curerentValue+1 {
		recCalculateNumberOfPath(numerInputParsed, i+1, j, topReached)
	}
	if j > 0 && numerInputParsed[i][j-1] == curerentValue+1 {
		recCalculateNumberOfPath(numerInputParsed, i, j-1, topReached)
	}
	if j < len(numerInputParsed[i])-1 && numerInputParsed[i][j+1] == curerentValue+1 {
		recCalculateNumberOfPath(numerInputParsed, i, j+1, topReached)
	}
}

type coordinate struct {
	x, y int
}
